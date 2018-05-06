"""
  Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

  Permission is hereby granted, free of charge, to any person obtaining a copy of this
  software and associated documentation files (the "Software"), to deal in the Software
  without restriction, including without limitation the rights to use, copy, modify,
  merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from cfnlint import CloudFormationLintRule
from cfnlint import RuleMatch


class CodepipelineStageActions(CloudFormationLintRule):
    """Check if CodePipeline Stage Actions are set up properly."""
    id = 'E2541'
    shortdesc = 'CodePipeline Stage Actions'
    description = 'See if CodePipeline stage actions are set correctly'
    tags = ['base', 'resources', 'codepipeline']

    VALID_OWNER_STRINGS = {'AWS', 'ThirdParty', 'Custom'}

    CONSTRAINTS = {
        'AWS': {
            'Source': {
                'S3': {
                    'InputArtifactRange': 0,
                    'OutputArtifactRange': 1,
                },
                'CodeCommit': {
                    'InputArtifactRange': 0,
                    'OutputArtifactRange': 1,
                }
            },
            'Build': {
                'CodeBuild': {
                    'InputArtifactRange': 1,
                    'OutputArtifactRange': (0, 1),
                },
            },
            'Test': {
                'CodeBuild': {
                    'InputArtifactRange': 1,
                    'OutputArtifactRange': (0, 1),
                }
            },
            'Approval': {
                'Manual': {
                    'InputArtifactRange': 0,
                    'OutputArtifactRange': 0,
                }
            },
            'Deploy': {
                'CloudFormation': {
                    'InputArtifactRange': (0, 10),
                    'OutputArtifactRange': (0, 1),
                },
                'CodeDeploy': {
                    'InputArtifactRange': 1,
                    'OutputArtifactRange': 0,
                },
                'ElasticBeanstalk': {
                    'InputArtifactRange': 1,
                    'OutputArtifactRange': 0,
                },
                'OpsWorks': {
                    'InputArtifactRange': 1,
                    'OutputArtifactRange': 0,
                },
                'ECS': {
                    'InputArtifactRange': 1,
                    'OutputArtifactRange': 0,
                },
            },
            'Invoke': {
                'Lambda': {
                    'InputArtifactRange': (0, 5),
                    'OutputArtifactRange': (0, 5),
                }
            }
        },
        'ThirdParty': {
            'Source': {
                'GitHub': {
                    'InputArtifactRange': 0,
                    'OutputArtifactRange': 1,
                }
            },
        },
    }

    KEY_MAP = {
        'InputArtifacts': 'InputArtifactRange',
        'OutputArtifacts': 'OutputArtifactRange',
    }

    def check_artifact_counts(self, action, artifact_type, path):
        """Check that artifact counts are within valid ranges."""
        matches = []

        owner = action['ActionTypeId']['Owner']
        if owner not in self.CONSTRAINTS.keys():
            return matches

        category = action['ActionTypeId']['Category']
        provider = action['ActionTypeId']['Provider']
        constraints = self.CONSTRAINTS[owner][category][provider]
        artifact_count = len(action.get(artifact_type, []))

        constraint_key = self.KEY_MAP[artifact_type]
        if isinstance(constraints[constraint_key], tuple):
            min_, max_ = constraints[constraint_key]
            if not (min_ <= artifact_count <= max_):
                message = (
                    'Action "{action}" declares {number} {artifact_type} which is not in '
                    'expected range [{a}, {b}].'
                ).format(
                    action=action['Name'],
                    number=artifact_count,
                    artifact_type=artifact_type,
                    a=min_,
                    b=max_
                )
                matches.append(RuleMatch(
                    path + [artifact_type],
                    message
                ))
        else:
            if artifact_count != constraints[constraint_key]:
                message = (
                    'Action "{action}" declares {number} {artifact_type} which is less than '
                    'expected [{a}].'
                ).format(
                    action=action['Name'],
                    number=artifact_count,
                    artifact_type=artifact_type,
                    a=constraints[constraint_key]
                )
                matches.append(RuleMatch(
                    path + [artifact_type],
                    message
                ))

        return matches

    def check_owner(self, action, path):
        """Check that action type owner is valid."""
        matches = []

        owner = action['ActionTypeId']['Owner']
        if owner not in self.VALID_OWNER_STRINGS:
            message = (
                'For all currently supported action types, the only valid owner '
                'strings are {owners}'
            ).format(
                owners=', '.join(list(self.VALID_OWNER_STRINGS))
            )
            matches.append(RuleMatch(
                path + ['ActionTypeId', 'Owner'],
                message
            ))

        return matches

    def check_version(self, action, path):
        """Check that action type version is valid."""
        matches = []

        if action['ActionTypeId']['Version'] != 1:
            message = 'For all currently supported action types, the only valid version is 1.'
            matches.append(RuleMatch(
                path + ['ActionTypeId', 'Version'],
                message
            ))

        return matches

    def check_names_unique(self, action, path, action_names):
        """Check that action names are unique."""
        matches = []

        if action['Name'] in action_names:
            message = 'All action names within a stage must be unique. ({name})'.format(
                name=action['Name']
            )
            matches.append(RuleMatch(path + ['Name'], message))
        action_names.add(action['Name'])

        return matches

    def match(self, cfn):
        """Check that stage actions are set up properly."""
        matches = list()

        resources = cfn.get_resource_properties(['AWS::CodePipeline::Pipeline'])
        for resource in resources:
            path = resource['Path']
            properties = resource['Value']

            for sidx, stage in enumerate(properties['Stages']):
                stage_path = path + ['Stages', sidx]
                action_names = set()
                for aidx, action in enumerate(stage['Actions']):
                    action_path = stage_path + ['Actions', aidx]

                    matches.extend(self.check_names_unique(action, action_path, action_names))
                    matches.extend(self.check_version(action, action_path))
                    matches.extend(self.check_owner(action, action_path))
                    matches.extend(self.check_artifact_counts(action, 'InputArtifacts', action_path))
                    matches.extend(self.check_artifact_counts(action, 'OutputArtifacts', action_path))

        return matches
