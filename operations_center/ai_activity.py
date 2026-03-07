agents = [

"auditor_agent",
"optimizer_agent",
"self_heal",
"marketing_engine"

]

def ai_status():

    return {

        "active_agents": agents,
        "count": len(agents)

    }
