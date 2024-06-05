#!/bin/bash

function parse_options() {
	while [[ $# -gt 0 ]]; do
		key="$1"
		case $key in
		-n | --number)
			NUMBER="$2"
			shift # past argument
			shift # past value
			;;
		*)
			shift # past argument
			;;
		esac
	done
}

function display_help() {
	echo "Usage: $0 -n <number>|--number=<number>"
	echo "Search for the top <number> most frequent k-mers in each individual gene."
	echo "Options:"
	echo "  -n <number>|--number=<number>  The number of most frequent k-mers to search for."
	echo "  -h|--help                        Display this help message and exit."
}

parse_options "$@"

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
	display_help
	exit 0
fi

if [ -z "$NUMBER" ]; then
	echo "Error: Please specify the number of most frequent k-mers to search for using -n or --number"
	exit 1
fi

cut -d , -f 6 all_GB_genes.log | sort | uniq -c | sort -k2nr |
	awk '{print $2}' | head -n "$NUMBER" |
	xargs -I {} grep -w {} all_GB_genes.log
