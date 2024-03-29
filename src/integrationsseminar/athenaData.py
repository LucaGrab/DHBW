import boto3
import time

CLIENT = boto3.client("athena")

DATABASE_NAME = "athena_tutorial"
RESULT_OUTPUT_LOCATION = "s3://learnaws-athena-tutorial/queries/"
TABLE_DDL = "funding_data.ddl"
TABLE_NAME = "funding_data"


def has_query_succeeded(execution_id):
    state = "RUNNING"
    max_execution = 5

    while max_execution > 0 and state in ["RUNNING", "QUEUED"]:
        max_execution -= 1
        response = CLIENT.get_query_execution(QueryExecutionId=execution_id)
        if (
            "QueryExecution" in response
            and "Status" in response["QueryExecution"]
            and "State" in response["QueryExecution"]["Status"]
        ):
            state = response["QueryExecution"]["Status"]["State"]
            if state == "SUCCEEDED":
                return True

        time.sleep(30)

    return False


def create_database():
    response = CLIENT.start_query_execution(
        QueryString=f"create database {DATABASE_NAME}",
        ResultConfiguration={"OutputLocation": RESULT_OUTPUT_LOCATION}
    )

    return response["QueryExecutionId"]


def create_table():
    with open(TABLE_DDL) as ddl:
        response = CLIENT.start_query_execution(
            QueryString=ddl.read(),
            ResultConfiguration={"OutputLocation": RESULT_OUTPUT_LOCATION}
        )

        return response["QueryExecutionId"]


def get_num_rows():
    query = f"SELECT COUNT(*) from {DATABASE_NAME}.{TABLE_NAME}"
    response = CLIENT.start_query_execution(
        QueryString=query,
        ResultConfiguration={"OutputLocation": RESULT_OUTPUT_LOCATION}
    )

    return response["QueryExecutionId"]


def get_query_results(execution_id):
    response = CLIENT.get_query_results(
        QueryExecutionId=execution_id
    )

    results = response['ResultSet']['Rows']
    return results


def main():
    """
    # 1. Create Database
    execution_id = create_database()
    print(f"Checking query execution for: {execution_id}")

    # 2. Check query execution
    query_status = has_query_succeeded(execution_id=execution_id)
    print(f"Query state: {query_status}")

    # 3. Create Table
    execution_id = create_table()
    print(f"Create Table execution id: {execution_id}")

    # 4. Check query execution
    query_status = has_query_succeeded(execution_id=execution_id)
    print(f"Query state: {query_status}")
"""
    # 5. Query Athena table
    execution_id = get_num_rows()
    print(f"Get Num Rows execution id: {execution_id}")

    query_status = has_query_succeeded(execution_id=execution_id)
    print(f"Query state: {query_status}")

    # 6. Query Results
    print(get_query_results(execution_id=execution_id))


if __name__ == "__main__":
    main()