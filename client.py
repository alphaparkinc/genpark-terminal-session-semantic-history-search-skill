class TerminalSessionSemanticHistorySearchClient:
    def search_cli_history(self, natural_language_query='find all docker containers using more than 2GB memory', session_shell='zsh'):
        return {
            'search_id': 'trm_hst_8812',
            'query': natural_language_query,
            'suggested_cli_command': 'docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}" | awk -F"/" "\$1 ~ /GiB/ {print \$0}"',
            'relevance_score': 0.94,
            'previously_executed': True,
            'last_exit_code': 0,
            'execution_safety_grade': 'READ_ONLY_INSPECT',
            'telemetry_url': 'https://productivity.developer.genpark.ai/warp/trm_hst_8812.json'
        }
