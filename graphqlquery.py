import requests
import json
import pandas as pd

query = """ query Proposals {
  proposals(first: 20, skip: 0, where:{space:"gitcoindao.eth"}, orderBy: "created", orderDirection: desc) {
    id
    title
    body
    choices
    start
    end
    snapshot
    state
    author
    space {
      id
      name
    }
  }
}
"""

json_response = requests.get(f'https://hub.snapshot.org/graphql', headers={'Accept': 'application/json'}, json={'query': query})

print(json_response.status_code)
print(json_response.text)

json_data = json.loads(json_response.text)

df_data = json_data["data"]["proposals"]
df = pd.DataFrame(df_data)
print(df)
