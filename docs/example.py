from config import USERNAME, PASSWORD
from rtbhouse_sdk.reports_api import ReportsApiSession

if __name__ == '__main__':
    api = ReportsApiSession(USERNAME, PASSWORD)
    print(api.get_user_info())