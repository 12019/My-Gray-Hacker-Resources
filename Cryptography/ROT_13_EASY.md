VAR=$(cat data.txt)
echo "$VAR"
alias rot13="tr A-Za-z N-ZA-Mn-za-m"
echo "$VAR" | rot13
