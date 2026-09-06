from client import TerminalSessionSemanticHistorySearchClient

def main():
    client = TerminalSessionSemanticHistorySearchClient()
    res = client.search_cli_history()
    print('Terminal History Search: ' + res['search_id'] + ' (Relevance: ' + str(res['relevance_score']) + ')')
    print('Suggested Command: ' + res['suggested_cli_command'])
    print('Telemetry URL: ' + res['telemetry_url'])

if __name__ == '__main__':
    main()
