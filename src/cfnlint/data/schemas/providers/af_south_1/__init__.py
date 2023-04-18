# pylint: disable=too-many-lines
cached = [
    "aws-apigatewayv2-integration.json",
    "aws-apigatewayv2-apimapping.json",
    "aws-sso-assignment.json",
    "aws-glue-partition.json",
    "aws-ec2-transitgatewayroutetablepropagation.json",
    "aws-apigateway-basepathmapping.json",
    "aws-guardduty-filter.json",
    "aws-ecs-service.json",
    "aws-ram-resourceshare.json",
    "aws-dynamodb-table.json",
    "aws-ec2-securitygroupegress.json",
    "aws-ec2-localgatewayroutetablevpcassociation.json",
    "aws-config-organizationconfigrule.json",
    "aws-networkmanager-transitgatewaypeering.json",
    "aws-config-configurationrecorder.json",
    "aws-ec2-networkperformancemetricsubscription.json",
    "aws-cloudfront-continuousdeploymentpolicy.json",
    "aws-ecr-replicationconfiguration.json",
    "aws-appconfig-extensionassociation.json",
    "aws-s3outposts-accesspoint.json",
    "aws-ec2-ipampoolcidr.json",
    "aws-redshift-clustersubnetgroup.json",
    "aws-rds-dbinstance.json",
    "aws-ec2-vpcdhcpoptionsassociation.json",
    "aws-apigateway-model.json",
    "aws-apigatewayv2-integrationresponse.json",
    "aws-ec2-networkacl.json",
    "aws-logs-resourcepolicy.json",
    "aws-lex-botversion.json",
    "aws-servicecatalog-launchnotificationconstraint.json",
    "aws-ec2-networkaclentry.json",
    "aws-ec2-networkinsightsaccessscopeanalysis.json",
    "aws-transfer-certificate.json",
    "aws-connect-instance.json",
    "aws-apigateway-documentationpart.json",
    "aws-cloudwatch-compositealarm.json",
    "aws-route53resolver-firewalldomainlist.json",
    "aws-appconfig-application.json",
    "aws-lambda-url.json",
    "aws-datasync-locationfsxwindows.json",
    "aws-apigateway-requestvalidator.json",
    "aws-autoscaling-warmpool.json",
    "aws-applicationautoscaling-scalabletarget.json",
    "aws-apigatewayv2-model.json",
    "aws-config-storedquery.json",
    "aws-acmpca-permission.json",
    "aws-transfer-server.json",
    "aws-apigateway-domainname.json",
    "aws-ecs-primarytaskset.json",
    "aws-fms-resourceset.json",
    "aws-autoscaling-autoscalinggroup.json",
    "aws-wafv2-regexpatternset.json",
    "aws-eks-fargateprofile.json",
    "aws-route53-dnssec.json",
    "aws-ec2-transitgatewayroutetable.json",
    "aws-controltower-enabledcontrol.json",
    "aws-networkmanager-connectattachment.json",
    "aws-route53-recordset.json",
    "aws-elasticache-securitygroup.json",
    "aws-backup-framework.json",
    "aws-cloudtrail-eventdatastore.json",
    "aws-kinesisfirehose-deliverystream.json",
    "aws-ec2-networkinsightsaccessscope.json",
    "aws-sagemaker-coderepository.json",
    "aws-imagebuilder-component.json",
    "aws-ses-configurationseteventdestination.json",
    "aws-glue-connection.json",
    "aws-appmesh-route.json",
    "aws-organizations-resourcepolicy.json",
    "aws-wafregional-webaclassociation.json",
    "aws-ec2-transitgatewaymulticastgroupsource.json",
    "aws-lex-bot.json",
    "aws-transfer-profile.json",
    "aws-databrew-recipe.json",
    "aws-apigateway-usageplankey.json",
    "aws-fms-policy.json",
    "aws-cloudfront-realtimelogconfig.json",
    "aws-sagemaker-pipeline.json",
    "aws-cloudtrail-channel.json",
    "aws-lakeformation-datacellsfilter.json",
    "aws-datasync-locationhdfs.json",
    "aws-events-archive.json",
    "aws-msk-cluster.json",
    "aws-codepipeline-pipeline.json",
    "aws-config-configurationaggregator.json",
    "aws-imagebuilder-imagepipeline.json",
    "aws-elasticloadbalancingv2-listenercertificate.json",
    "aws-cloudformation-moduleversion.json",
    "aws-cloud9-environmentec2.json",
    "aws-route53resolver-resolverruleassociation.json",
    "aws-fsx-storagevirtualmachine.json",
    "aws-synthetics-canary.json",
    "aws-sns-subscription.json",
    "aws-appmesh-mesh.json",
    "aws-ec2-natgateway.json",
    "aws-internetmonitor-monitor.json",
    "aws-transfer-workflow.json",
    "aws-appconfig-deploymentstrategy.json",
    "aws-glue-devendpoint.json",
    "aws-sagemaker-modelpackage.json",
    "aws-customerprofiles-integration.json",
    "aws-networkmanager-connectpeer.json",
    "aws-elasticache-usergroup.json",
    "aws-imagebuilder-imagerecipe.json",
    "aws-apigateway-restapi.json",
    "aws-opsworks-elasticloadbalancerattachment.json",
    "aws-appmesh-virtualservice.json",
    "aws-s3objectlambda-accesspointpolicy.json",
    "aws-networkmanager-transitgatewayregistration.json",
    "aws-elasticache-replicationgroup.json",
    "aws-cloudformation-moduledefaultversion.json",
    "aws-sso-permissionset.json",
    "aws-glue-job.json",
    "aws-servicecatalog-cloudformationprovisionedproduct.json",
    "aws-glue-table.json",
    "aws-logs-metricfilter.json",
    "aws-lambda-function.json",
    "aws-sns-topic.json",
    "aws-backup-backupselection.json",
    "aws-datasync-locationfsxlustre.json",
    "aws-sagemaker-app.json",
    "aws-ec2-vpcgatewayattachment.json",
    "aws-cloudtrail-trail.json",
    "aws-ec2-vpnconnectionroute.json",
    "aws-ec2-internetgateway.json",
    "aws-ec2-gatewayroutetableassociation.json",
    "aws-wafv2-ipset.json",
    "aws-ssm-document.json",
    "aws-iam-role.json",
    "aws-events-apidestination.json",
    "aws-dms-endpoint.json",
    "aws-cloudfront-cloudfrontoriginaccessidentity.json",
    "aws-sagemaker-endpointconfig.json",
    "aws-appmesh-gatewayroute.json",
    "aws-apigateway-apikey.json",
    "aws-networkmanager-transitgatewayroutetableattachment.json",
    "aws-autoscaling-launchconfiguration.json",
    "aws-apigateway-clientcertificate.json",
    "aws-kinesisanalyticsv2-application.json",
    "aws-lambda-alias.json",
    "aws-ec2-transitgatewaymulticastdomainassociation.json",
    "aws-s3outposts-endpoint.json",
    "aws-ec2-transitgatewayroutetableassociation.json",
    "aws-appconfig-environment.json",
    "aws-imagebuilder-image.json",
    "aws-elasticache-securitygroupingress.json",
    "aws-wafregional-xssmatchset.json",
    "aws-rds-dbproxytargetgroup.json",
    "aws-cloudwatch-dashboard.json",
    "aws-cloudwatch-alarm.json",
    "aws-guardduty-member.json",
    "aws-groundstation-missionprofile.json",
    "aws-cloudformation-customresource.json",
    "aws-wafv2-rulegroup.json",
    "aws-sagemaker-modelpackagegroup.json",
    "aws-ses-configurationset.json",
    "aws-elasticache-parametergroup.json",
    "aws-networkfirewall-loggingconfiguration.json",
    "aws-glue-classifier.json",
    "aws-codedeploy-deploymentgroup.json",
    "aws-sagemaker-inferenceexperiment.json",
    "aws-cloudformation-stackset.json",
    "aws-ec2-route.json",
    "aws-fis-experimenttemplate.json",
    "aws-cloudformation-hookversion.json",
    "aws-xray-resourcepolicy.json",
    "aws-servicecatalog-launchtemplateconstraint.json",
    "aws-wafv2-loggingconfiguration.json",
    "aws-backup-backupplan.json",
    "aws-imagebuilder-distributionconfiguration.json",
    "aws-lakeformation-permissions.json",
    "aws-cloudfront-publickey.json",
    "aws-lex-botalias.json",
    "aws-identitystore-group.json",
    "aws-datasync-task.json",
    "aws-ecs-taskdefinition.json",
    "aws-sagemaker-model.json",
    "aws-ses-vdmattributes.json",
    "aws-identitystore-groupmembership.json",
    "aws-appsync-functionconfiguration.json",
    "aws-ec2-spotfleet.json",
    "aws-glue-schemaversion.json",
    "aws-sagemaker-space.json",
    "aws-fms-notificationchannel.json",
    "aws-msk-batchscramsecret.json",
    "aws-dms-certificate.json",
    "aws-s3-bucket.json",
    "aws-guardduty-ipset.json",
    "aws-servicediscovery-httpnamespace.json",
    "aws-emr-securityconfiguration.json",
    "aws-cloudwatch-insightrule.json",
    "aws-apigateway-usageplan.json",
    "aws-batch-schedulingpolicy.json",
    "aws-databrew-project.json",
    "aws-athena-workgroup.json",
    "aws-sagemaker-imageversion.json",
    "aws-apigatewayv2-api.json",
    "aws-detective-graph.json",
    "aws-servicecatalog-portfolioshare.json",
    "aws-connect-integrationassociation.json",
    "aws-networkmanager-customergatewayassociation.json",
    "aws-iam-servercertificate.json",
    "aws-events-eventbus.json",
    "aws-ssm-maintenancewindowtarget.json",
    "aws-voiceid-domain.json",
    "aws-apigateway-authorizer.json",
    "aws-databrew-schedule.json",
    "aws-connect-approvedorigin.json",
    "aws-ses-contactlist.json",
    "aws-connect-securitykey.json",
    "aws-cloudformation-publisher.json",
    "aws-rds-dbsecuritygroupingress.json",
    "aws-ec2-transitgatewaymulticastgroupmember.json",
    "aws-ec2-volumeattachment.json",
    "aws-glue-securityconfiguration.json",
    "aws-databrew-ruleset.json",
    "aws-applicationinsights-application.json",
    "aws-ecs-clustercapacityproviderassociations.json",
    "aws-appconfig-configurationprofile.json",
    "aws-route53resolver-firewallrulegroup.json",
    "aws-msk-configuration.json",
    "aws-ec2-transitgateway.json",
    "aws-ec2-vpcendpointservicepermissions.json",
    "aws-ssm-maintenancewindowtask.json",
    "aws-ec2-transitgatewaymulticastdomain.json",
    "aws-eks-cluster.json",
    "aws-codebuild-project.json",
    "aws-efs-filesystem.json",
    "aws-logs-querydefinition.json",
    "aws-iam-instanceprofile.json",
    "aws-datasync-locationnfs.json",
    "aws-sagemaker-domain.json",
    "aws-certificatemanager-certificate.json",
    "aws-glue-schemaversionmetadata.json",
    "aws-sdb-domain.json",
    "aws-ec2-subnetroutetableassociation.json",
    "aws-servicecatalog-serviceactionassociation.json",
    "aws-sagemaker-notebookinstancelifecycleconfig.json",
    "aws-imagebuilder-containerrecipe.json",
    "aws-connect-rule.json",
    "aws-efs-accesspoint.json",
    "aws-redshift-clustersecuritygroupingress.json",
    "aws-servicecatalogappregistry-attributegroupassociation.json",
    "aws-elasticloadbalancingv2-loadbalancer.json",
    "aws-opensearchservice-domain.json",
    "aws-servicediscovery-instance.json",
    "aws-elasticsearch-domain.json",
    "aws-apigatewayv2-deployment.json",
    "aws-servicecatalog-stacksetconstraint.json",
    "aws-servicecatalog-tagoption.json",
    "aws-servicediscovery-privatednsnamespace.json",
    "aws-servicecatalog-launchroleconstraint.json",
    "aws-secretsmanager-resourcepolicy.json",
    "aws-cloudformation-hookdefaultversion.json",
    "aws-config-configrule.json",
    "aws-ec2-networkinsightsanalysis.json",
    "aws-ec2-clientvpnroute.json",
    "aws-ecs-taskset.json",
    "aws-appsync-apikey.json",
    "aws-cloudformation-typeactivation.json",
    "aws-groundstation-dataflowendpointgroup.json",
    "aws-acmpca-certificateauthorityactivation.json",
    "aws-guardduty-threatintelset.json",
    "aws-macie-allowlist.json",
    "aws-ec2-vpc.json",
    "aws-dms-replicationsubnetgroup.json",
    "aws-s3outposts-bucket.json",
    "aws-route53-recordsetgroup.json",
    "aws-ec2-localgatewayroute.json",
    "aws-cloudformation-publictypeversion.json",
    "aws-opsworks-app.json",
    "aws-kinesis-stream.json",
    "aws-backup-reportplan.json",
    "aws-batch-jobdefinition.json",
    "aws-iam-samlprovider.json",
    "aws-appflow-connector.json",
    "aws-cloudfront-keygroup.json",
    "aws-ec2-transitgatewayattachment.json",
    "aws-codedeploy-deploymentconfig.json",
    "aws-networkmanager-globalnetwork.json",
    "aws-connect-tasktemplate.json",
    "aws-servicecatalogappregistry-application.json",
    "aws-networkmanager-site.json",
    "aws-neptune-dbcluster.json",
    "aws-backup-backupvault.json",
    "aws-ec2-customergateway.json",
    "aws-scheduler-schedule.json",
    "aws-waf-bytematchset.json",
    "aws-ec2-host.json",
    "aws-lambda-codesigningconfig.json",
    "aws-systemsmanagersap-application.json",
    "aws-dms-replicationtask.json",
    "aws-ec2-routetable.json",
    "aws-rds-dbproxyendpoint.json",
    "aws-datasync-locationsmb.json",
    "aws-resiliencehub-app.json",
    "aws-redshift-clusterparametergroup.json",
    "aws-organizations-policy.json",
    "aws-glue-trigger.json",
    "aws-globalaccelerator-listener.json",
    "aws-signer-signingprofile.json",
    "aws-ec2-vpcpeeringconnection.json",
    "aws-networkfirewall-rulegroup.json",
    "aws-kms-key.json",
    "aws-route53resolver-resolverdnssecconfig.json",
    "aws-route53resolver-firewallrulegroupassociation.json",
    "aws-route53resolver-resolverqueryloggingconfig.json",
    "aws-ec2-subnet.json",
    "aws-cloudtrail-resourcepolicy.json",
    "aws-s3objectlambda-accesspoint.json",
    "aws-elasticbeanstalk-configurationtemplate.json",
    "aws-sqs-queuepolicy.json",
    "aws-appsync-domainnameapiassociation.json",
    "aws-apigateway-account.json",
    "aws-wafv2-webacl.json",
    "aws-globalaccelerator-endpointgroup.json",
    "aws-ec2-transitgatewayconnect.json",
    "aws-networkmanager-sitetositevpnattachment.json",
    "aws-ec2-securitygroup.json",
    "aws-ec2-capacityreservationfleet.json",
    "aws-opsworks-volume.json",
    "aws-ses-emailidentity.json",
    "aws-iam-usertogroupaddition.json",
    "aws-events-rule.json",
    "aws-databrew-dataset.json",
    "aws-ec2-vpngatewayroutepropagation.json",
    "aws-cloudfront-function.json",
    "aws-apigateway-method.json",
    "aws-wafregional-regexpatternset.json",
    "aws-ssm-patchbaseline.json",
    "aws-servicediscovery-service.json",
    "aws-customerprofiles-objecttype.json",
    "aws-cloudfront-monitoringsubscription.json",
    "aws-efs-mounttarget.json",
    "aws-ec2-vpnconnection.json",
    "aws-servicediscovery-publicdnsnamespace.json",
    "aws-networkmanager-vpcattachment.json",
    "aws-iam-user.json",
    "aws-emr-instancegroupconfig.json",
    "aws-stepfunctions-activity.json",
    "aws-ec2-localgatewayroutetablevirtualinterfacegroupassociation.json",
    "aws-s3-bucketpolicy.json",
    "aws-appsync-graphqlschema.json",
    "aws-redshift-cluster.json",
    "aws-codebuild-sourcecredential.json",
    "aws-emr-instancefleetconfig.json",
    "aws-emr-cluster.json",
    "aws-apigatewayv2-domainname.json",
    "aws-rds-dbcluster.json",
    "aws-servicecatalog-resourceupdateconstraint.json",
    "aws-transfer-agreement.json",
    "aws-chatbot-slackchannelconfiguration.json",
    "aws-cloudfront-distribution.json",
    "aws-elasticache-subnetgroup.json",
    "aws-xray-group.json",
    "aws-oam-link.json",
    "aws-sagemaker-endpoint.json",
    "aws-networkfirewall-firewall.json",
    "aws-ses-template.json",
    "aws-kms-replicakey.json",
    "aws-redshift-clustersecuritygroup.json",
    "aws-route53-cidrcollection.json",
    "aws-ecr-pullthroughcacherule.json",
    "aws-glue-mltransform.json",
    "aws-appconfig-hostedconfigurationversion.json",
    "aws-datasync-locationefs.json",
    "aws-ec2-localgatewayroutetable.json",
    "aws-apigateway-resource.json",
    "aws-sagemaker-appimageconfig.json",
    "aws-macie-session.json",
    "aws-elasticloadbalancingv2-targetgroup.json",
    "aws-pipes-pipe.json",
    "aws-cloudformation-macro.json",
    "aws-sagemaker-workteam.json",
    "aws-secretsmanager-secret.json",
    "aws-elasticache-user.json",
    "aws-sagemaker-image.json",
    "aws-logs-subscriptionfilter.json",
    "aws-codedeploy-application.json",
    "aws-dms-eventsubscription.json",
    "aws-lakeformation-principalpermissions.json",
    "aws-datasync-locations3.json",
    "aws-autoscaling-lifecyclehook.json",
    "aws-fsx-datarepositoryassociation.json",
    "aws-ec2-networkinterface.json",
    "aws-sagemaker-featuregroup.json",
    "aws-appsync-resolver.json",
    "aws-route53resolver-resolverqueryloggingconfigassociation.json",
    "aws-lambda-eventinvokeconfig.json",
    "aws-lambda-layerversion.json",
    "aws-rds-optiongroup.json",
    "aws-opsworks-userprofile.json",
    "aws-glue-schema.json",
    "aws-customerprofiles-domain.json",
    "aws-ssm-maintenancewindow.json",
    "aws-lakeformation-tagassociation.json",
    "aws-ec2-ipamresourcediscovery.json",
    "aws-imagebuilder-infrastructureconfiguration.json",
    "aws-route53resolver-resolverendpoint.json",
    "aws-networkmanager-link.json",
    "aws-sagemaker-notebookinstance.json",
    "aws-sso-instanceaccesscontrolattributeconfiguration.json",
    "aws-wafregional-bytematchset.json",
    "aws-cloudwatch-anomalydetector.json",
    "aws-ec2-subnetnetworkaclassociation.json",
    "aws-servicecatalog-serviceaction.json",
    "aws-cloudfront-originaccesscontrol.json",
    "aws-secretsmanager-rotationschedule.json",
    "aws-lambda-permission.json",
    "aws-networkfirewall-firewallpolicy.json",
    "aws-eks-identityproviderconfig.json",
    "aws-ec2-ipamresourcediscoveryassociation.json",
    "aws-servicecatalogappregistry-attributegroup.json",
    "aws-ec2-clientvpntargetnetworkassociation.json",
    "aws-appsync-graphqlapi.json",
    "aws-ec2-egressonlyinternetgateway.json",
    "aws-ec2-vpccidrblock.json",
    "aws-iam-virtualmfadevice.json",
    "aws-ec2-networkinsightspath.json",
    "aws-acmpca-certificateauthority.json",
    "aws-athena-preparedstatement.json",
    "aws-autoscaling-scheduledaction.json",
    "aws-apigatewayv2-route.json",
    "aws-lakeformation-resource.json",
    "aws-detective-memberinvitation.json",
    "aws-ec2-ipamscope.json",
    "aws-ec2-vpcendpoint.json",
    "aws-rds-eventsubscription.json",
    "aws-config-aggregationauthorization.json",
    "aws-datasync-agent.json",
    "aws-resiliencehub-resiliencypolicy.json",
    "aws-logs-loggroup.json",
    "aws-ec2-placementgroup.json",
    "aws-organizations-account.json",
    "aws-ecr-repository.json",
    "aws-ses-dedicatedippool.json",
    "aws-appconfig-extension.json",
    "aws-lex-resourcepolicy.json",
    "aws-glue-registry.json",
    "aws-ec2-keypair.json",
    "aws-fsx-filesystem.json",
    "aws-ec2-eipassociation.json",
    "aws-elasticbeanstalk-application.json",
    "aws-dlm-lifecyclepolicy.json",
    "aws-ec2-capacityreservation.json",
    "aws-elasticloadbalancing-loadbalancer.json",
    "aws-transfer-user.json",
    "aws-rds-dbclusterparametergroup.json",
    "aws-appmesh-virtualrouter.json",
    "aws-scheduler-schedulegroup.json",
    "aws-fsx-snapshot.json",
    "aws-route53-keysigningkey.json",
    "aws-config-remediationconfiguration.json",
    "aws-events-connection.json",
    "aws-athena-datacatalog.json",
    "aws-glue-workflow.json",
    "aws-apigatewayv2-authorizer.json",
    "aws-sagemaker-userprofile.json",
    "aws-ec2-prefixlist.json",
    "aws-ec2-instance.json",
    "aws-networkmanager-device.json",
    "aws-elasticbeanstalk-applicationversion.json",
    "aws-appmesh-virtualgateway.json",
    "aws-waf-sqlinjectionmatchset.json",
    "aws-ec2-transitgatewayvpcattachment.json",
    "aws-ec2-flowlog.json",
    "aws-amazonmq-broker.json",
    "aws-ssm-association.json",
    "aws-ec2-clientvpnendpoint.json",
    "aws-cloudfront-responseheaderspolicy.json",
    "aws-kms-alias.json",
    "aws-route53resolver-resolverrule.json",
    "aws-transfer-connector.json",
    "aws-appmesh-virtualnode.json",
    "aws-apigateway-documentationversion.json",
    "aws-wafv2-webaclassociation.json",
    "aws-oam-sink.json",
    "aws-codebuild-reportgroup.json",
    "aws-apigateway-gatewayresponse.json",
    "aws-ec2-enclavecertificateiamroleassociation.json",
    "aws-fsx-volume.json",
    "aws-acmpca-certificate.json",
    "aws-ec2-ipamallocation.json",
    "aws-workspaces-workspace.json",
    "aws-datasync-locationobjectstorage.json",
    "aws-ecs-capacityprovider.json",
    "aws-elasticache-cachecluster.json",
    "aws-sagemaker-modelcard.json",
    "aws-logs-destination.json",
    "aws-eks-nodegroup.json",
    "aws-organizations-organizationalunit.json",
    "aws-appsync-datasource.json",
    "aws-sqs-queue.json",
    "aws-ec2-securitygroupingress.json",
    "aws-guardduty-detector.json",
    "aws-apigateway-stage.json",
    "aws-networkmanager-corenetwork.json",
    "aws-batch-computeenvironment.json",
    "aws-connect-instancestorageconfig.json",
    "aws-events-eventbuspolicy.json",
    "aws-apigateway-deployment.json",
    "aws-lakeformation-datalakesettings.json",
    "aws-autoscaling-scalingpolicy.json",
    "aws-groundstation-config.json",
    "aws-ecr-registrypolicy.json",
    "aws-rds-dbsecuritygroup.json",
    "aws-apigatewayv2-routeresponse.json",
    "aws-cloudwatch-metricstream.json",
    "aws-ssm-parameter.json",
    "aws-apigatewayv2-apigatewaymanagedoverrides.json",
    "aws-config-deliverychannel.json",
    "aws-certificatemanager-account.json",
    "aws-iam-oidcprovider.json",
    "aws-lakeformation-tag.json",
    "aws-servicecatalogappregistry-resourceassociation.json",
    "aws-ec2-vpngateway.json",
    "aws-cloudformation-stack.json",
    "aws-resourcegroups-group.json",
    "aws-cloudformation-resourcedefaultversion.json",
    "aws-signer-profilepermission.json",
    "aws-ec2-ipam.json",
    "aws-databrew-job.json",
    "aws-ec2-transitgatewaypeeringattachment.json",
    "aws-cloudfront-cachepolicy.json",
    "aws-appintegrations-dataintegration.json",
    "aws-rds-dbsubnetgroup.json",
    "aws-amazonmq-configuration.json",
    "aws-appconfig-deployment.json",
    "aws-accessanalyzer-analyzer.json",
    "aws-ec2-ec2fleet.json",
    "aws-dms-replicationinstance.json",
    "aws-servicecatalog-cloudformationproduct.json",
    "aws-ec2-vpcendpointservice.json",
    "aws-iam-managedpolicy.json",
    "aws-ec2-launchtemplate.json",
    "aws-cloudfront-originrequestpolicy.json",
    "aws-datasync-locationfsxontap.json",
    "aws-networkmanager-linkassociation.json",
    "aws-mediatailor-playbackconfiguration.json",
    "aws-elasticbeanstalk-environment.json",
    "aws-wafregional-sqlinjectionmatchset.json",
    "aws-lambda-version.json",
    "aws-ec2-dhcpoptions.json",
    "aws-ec2-ipampool.json",
    "aws-iam-servicelinkedrole.json",
    "aws-cloudformation-hooktypeconfig.json",
    "aws-ec2-volume.json",
    "aws-ec2-eip.json",
    "aws-cloudformation-resourceversion.json",
    "aws-apigatewayv2-stage.json",
    "aws-chatbot-microsoftteamschannelconfiguration.json",
    "aws-rds-dbproxy.json",
    "aws-rds-dbparametergroup.json",
    "aws-securityhub-hub.json",
    "aws-s3-accesspoint.json",
    "aws-s3outposts-bucketpolicy.json",
    "aws-batch-jobqueue.json",
    "aws-redshift-eventsubscription.json",
    "aws-cloudformation-waitconditionhandle.json",
    "aws-globalaccelerator-accelerator.json",
    "aws-eks-addon.json",
]
