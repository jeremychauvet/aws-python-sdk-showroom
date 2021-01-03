#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import sys
import boto3

# This function insert fake datas in queue defined bellow.
client = boto3.client("cognito-idp", region_name="eu-central-1")

def get_parameters():
    try:
        # Get all users pools.
        userPools = client.list_user_pools(
            MaxResults=10
        )

        for userPool in userPools["UserPools"]:
            print("USER_POOL_NAME : " + userPool["Name"])
            print("USER_POOL_ID : " + userPool["Id"])
            # For each userPool, describe his configuration.
            print("-------------------------------------------------------")

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))

if __name__ == "__main__":
    get_parameters()
