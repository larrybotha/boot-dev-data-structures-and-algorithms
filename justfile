default:
    just --list

watch filename:
    #!/usr/bin/env bash
    test_file=$(echo {{ filename }} | sed 's/\.py/_test\.py/')

    watchexec -w {{ filename }} "uv run python $test_file"
