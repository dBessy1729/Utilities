#!/bin/bash

cd /media/my_usb/Music/google/files
for file in *.zip ; do
    newfile=$(echo "${file}" | sed -e 's/^files.//' -e 's/.zip$//')
    echo ":${newfile}:"
    mkdir tmp
    rm -rf "${newfile}"
    mkdir "${newfile}"
    cp "${newfile}.zip" tmp
    cd tmp
    unzip "${newfile}.zip"
    find . -name '*.mp3' -exec cp {} "../${newfile}" ';'
    #find . -name '*.gif' -exec cp {} "../${newfile}" ';'
    cd ..
    rm -rf tmp
done
