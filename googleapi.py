# INTERNAL USE ONLY
# COPYRIGHTED GOOGLE CONTENT DO NOT DISTRIBUTE
# Copyright 2021 Google Inc. All Rights Reserved.

from webbrowser import get
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import OrderBy
from google.analytics.data_v1beta.types import RunReportRequest
import pandas as pd



#collavision download page = 309927857, creative cast firebase = 281054280, creative cast download page = 309886486, collavision firebase = 281875252
def run_report(property_id="281054280", start = None):
    credentials_json_path="client_key.json"
    Dates = []
    Active_Users = []
    New_Users = []
    Months = []

    client = BetaAnalyticsDataClient().from_service_account_json(credentials_json_path)

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

        # print(row.dimension_values[0].value, row.metric_values[0].value, row.metric_values[1].value, row.dimension_values[1].value)
    
    data_frame = pd.DataFrame({"Date": Dates, "Users": Active_Users, "New users": New_Users, "month": Months})

    return data_frame




def get_report(decision, timespan):

    ccd_code = "309886486"
    cvd_code = "309927857"
    ccf_code = "281054280"
    cvf_code = "281875252"

    if decision == 1:
        p_id = ccd_code
    elif decision == 2:
        p_id = cvd_code
    elif decision == 'A':
        p_id = ccf_code
    elif decision == 'B':
        p_id = cvf_code
    
    report = run_report(p_id, timespan)

    return report
    

