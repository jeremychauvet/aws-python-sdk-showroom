# Get key rotation status

This function insert fake datas in a SQS queue.
For testing purpose, datas insert are fake credit scores.

## Prerequisites

* You must create a "default" [named profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html).
* You must install [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html).
* Python 3

## How to run

At project root, please run `make insert-fake-data-in-queue`.

## Output example

```bash
[INFO] Message : FICO Score 10 - Equifax - 636
[INFO] Hash : 83e9573377810c315de2c0f0093eb995
[INFO] Message 0 of 10 sent successfully.
[INFO] Message : FICO Score 10 T - Equifax - 503
[INFO] Hash : 7b15a8262852413b9f118493f006536a
[INFO] Message 1 of 10 sent successfully.
[INFO] Message : FICO Score 10 - TransUnion - 557
[INFO] Hash : 8d87029324c5cd40c651e00c53beffeb
[INFO] Message 2 of 10 sent successfully.
[INFO] Message : VantageScore 3.0 - TransUnion - 427
[INFO] Hash : 2356a254db78f6e1fb7598a6705d3a7e
[INFO] Message 3 of 10 sent successfully.
[INFO] Message : Equifax Beacon 5.0 - Equifax - 818
[INFO] Hash : cfeb876c72f6a9748243f94413c249f3
[INFO] Message 4 of 10 sent successfully.
[INFO] Message : FICO Score 8 - Experian - 539
[INFO] Hash : c63fc28f37f0152f9fe5d86b3adaf720
[INFO] Message 5 of 10 sent successfully.
[INFO] Message : FICO Score 10 - Experian - 659
[INFO] Hash : f4f98e058061faa562568c28c3a89ae5
[INFO] Message 6 of 10 sent successfully.
[INFO] Message : FICO Score 8 - TransUnion - 599
[INFO] Hash : bb1f71f5a219a5cea1b569c626dae5d6
[INFO] Message 7 of 10 sent successfully.
[INFO] Message : FICO Score 10 - Experian - 664
[INFO] Hash : f61b98f7c824c8376d8742827d446621
[INFO] Message 8 of 10 sent successfully.
[INFO] Message : FICO Score 8 - Equifax - 520
[INFO] Hash : 552cca5ada2542e02a010d2039ff0c6c
[INFO] Message 9 of 10 sent successfully.
```
