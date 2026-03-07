from fastapi import APIRouter
from operations_center.system_monitor import system_status
from operations_center.revenue_graphs import revenue_data
from operations_center.ai_activity import ai_status
from operations_center.marketing_activity import marketing_stats
from operations_center.marketplace_activity import marketplace_stats

router = APIRouter()

@router.get("/operations")

def operations_dashboard():

    return {

        "system": system_status(),
        "revenue": revenue_data(),
        "ai": ai_status(),
        "marketing": marketing_stats(),
        "marketplace": marketplace_stats()

    }
