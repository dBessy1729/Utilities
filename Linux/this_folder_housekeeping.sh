cd $PWD

ls -al

find $PWD -maxdepth 1 -mtime +7 -type f -iname "*.csv" -exec ls -ltr {} \;

find $PWD -maxdepth 1 -mtime +7 -type f -exec mv  "{}" ./Archive \;
# find $PWD -maxdepth 1 -mtime +7 -type f -iname "*.csv" -exec rm {} \;

ls -al
