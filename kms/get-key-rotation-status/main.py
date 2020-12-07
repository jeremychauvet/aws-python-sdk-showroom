import boto3
import botocore

# This function list all KMS keys with no key rotation enable.

client = boto3.client("kms", region_name="eu-central-1")


def list_keys():
    try:
        return client.list_keys(Limit=100)
    except:
        print("[ERROR] Unable to retrive key list.")


if __name__ == "__main__":
    output = list_keys()
    for row in output["Keys"]:
        # Check key rotation status.
        try:
            response = client.get_key_rotation_status(KeyId=row["KeyId"])

            if response["KeyRotationEnabled"] == False:
                print(
                    "Key : "
                    + row["KeyId"]
                    + " - KeyRotationEnabled : "
                    + str(response["KeyRotationEnabled"])
                )
        except botocore.exceptions.ClientError as e:
            print("[ERROR]", e)
