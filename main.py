from utils import update_lds_opportunities
import gspread
from keys import GoogConfig

if __name__ == "__main__":
    GC = gspread.service_account_from_dict(GoogConfig.CREDENTIALS)

    update_lds_opportunities(google_client=GC)
