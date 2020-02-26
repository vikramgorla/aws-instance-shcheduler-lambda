import boto3
RDS = boto3.client('rds')
def lambda_handler(event, context):
    
    # Check that our inputs are valid
    try:
        clusters = event.get('clusters')
        action = event.get('action')
    except Exception as e:
        return "Exception! Failed with: {0}".format(e)
    
    if (not (action == "stop" or action == "start")) or (not isinstance(clusters, list)):
        return "clusters must be a list of strings, action must be \"Start\" or \"Stop\""
    
    # Filter through our databases, only get the clusters that are featured in our clusters list
    dbs = set([])
    rds_clusters = RDS.describe_db_clusters()
    for rds_cluster in rds_clusters['DBClusters']:
        for cluster in clusters:
            if cluster in rds_cluster['DBClusterIdentifier']:
                dbs.add(rds_cluster['DBClusterIdentifier'])
    
    # Apply our action
    for db in dbs:
        try:
            if action == "start":
                response = RDS.start_db_cluster(DBClusterIdentifier=db)
            else:
                response = RDS.stop_db_cluster(DBClusterIdentifier=db)
                
            print("{0} status: {1}".format(db, response['DBClusterStatus']))
        except Exception as e:
            print("Exception: {0}".format(e))
    
    return "Completed!"
