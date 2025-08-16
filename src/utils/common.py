from typing import Dict


def generate_headers(request: dict, token: str) -> Dict[str, str]:
     
    token,hy_user = token.split(',')

    agent_id = "naQivTmsDa"

    request["hy_source"] = "web"
    request["hy_user"] = hy_user
    request["agent_id"] = agent_id
      
    return {
        "Cookie": f"hy_source={request['hy_source']}; hy_user={request['hy_user']}; hy_token={token}",
        "Origin": "https://yuanbao.tencent.com",
        "Referer": f"https://yuanbao.tencent.com/chat/{request['agent_id']}",
        "X-Agentid": request["agent_id"],
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    }
