#!/bin/bash
NUMBER=6
# Parse command line options
parse_options() {
while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in
    -n|--number)
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

# Display help message
 display_help() {
  echo "Usage: $0 -n <number>|--number=<number>"
  echo "Search for the top <number> most frequent k-mers in each individual gene."
  echo "Options:"
  echo "  -n <number>|--number=<number>  The number of most frequent k-mers to search for. Default is 6."
  echo "  -h|--help                        Display this help message and exit."
}

parse_options "$@"

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
  display_help
  exit 0
fi



awk -F',' '{print $4}' all_GB_genes.log | sort | uniq -c | awk -v n="$NUMBER" '$1 >= n' | sort -k1 -n -r
