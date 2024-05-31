cut -d , -f 6 Final.log  |sort |  uniq -c | sort -k2n
cut -d , -f 4 Final.log  |sort |  uniq -c | sort -k1,1n | awk '{printJAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/}' | un -c

