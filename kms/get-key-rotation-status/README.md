# Get key rotation status

This function list key with no key rotation enable.
As this is a security issue, we recommand to remediate this point quicky. Full documentation [here](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

## Prerequisites

* You must create a "default" [named profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html).
* You must install [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html).
* Python 3

## How to run

At project root, please run `make get-key-rotation-status`.

## Output example

```bash
Key : xxyyzzaa-0000-1111-2222-bbccddeeffgg - KeyRotationEnabled : False
```
