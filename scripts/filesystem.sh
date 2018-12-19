# Determine the type of file
# Create the folder/file

if [ $1 = 'folder' ];
then
    mkdir $2

elif [ $1 = 'file' ];
then
    touch $2

else
    echo Invalid
fi
