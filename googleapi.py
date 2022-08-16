# INTERNAL USE ONLY


# API is still in beta beware of inaccurate outputs

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import OrderBy
from google.analytics.data_v1beta.types import RunReportRequest
import pandas as pd





def run_report(property_id=" ", start = None, credentials_json_path="client_key.json"):
    
    Dates = []
    Active_Users = []
    New_Users = []
    Months = []

    client = BetaAnalyticsDataClient().from_service_account_json(credentials_json_path)

    # If different dimentions and metrics are desired, make sure to look up the correct schemas at 
    # https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema 

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date"), Dimension(name = "month")],
        metrics=[Metric(name="activeUsers"), Metric(name = "newUsers")],
        date_ranges=[DateRange(start_date=start, end_date="today")],
        order_bys = [
            OrderBy(dimension = OrderBy.DimensionOrderBy(dimension_name = "date"), desc = False)
        ],
    )
    response = client.run_report(request)

    print("Report result:")
    for row in response.rows:
        Dates.append(int(row.dimension_values[0].value))
        Active_Users.append(int(row.metric_values[0].value))
        New_Users.append(int(row.metric_values[1].value))
        Months.append(int(row.dimension_values[1].value))

        # uncomment this below line to check if data points are missing
        # print(row.dimension_values[0].value, row.metric_values[0].value, row.metric_values[1].value, row.dimension_values[1].value)
    
    data_frame = pd.DataFrame({"Date": Dates, "Users": Active_Users, "New users": New_Users, "month": Months})

    return data_frame




def get_report(decision, timespan, path):

    # property IDs for CC, CV firebase as well as download page

    ccd_code = " " 
    cvd_code = " "
    ccf_code = " "
    cvf_code = " "

    # As of now download page api report was not needed, but could be easily implemented for future references.
    
    if decision == 1:
        p_id = ccd_code
    elif decision == 2:
        p_id = cvd_code
    elif decision == 'A':
        p_id = ccf_code
    elif decision == 'B':
        p_id = cvf_code
    
    report = run_report(p_id, timespan, path)

    return report
    

