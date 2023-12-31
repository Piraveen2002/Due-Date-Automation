# Change the current directory below
cd C:\

ls *.pdf -name > .\lists.txt
New-Item -Path .\result.txt -ItemType File 

if (test-path .\list.txt){
    foreach ($line in cat .\lists.txt){
        if (!(Select-String -Path .\list.txt -SimpleMatch $line)){
            Add-Content .\result.txt $line
        }
    }

    rm .\lists.txt
}
else{
    Rename-Item .\lists.txt .\list.txt
    cp .\list.txt .\result.txt 
    echo "Testing all of them!"
}

foreach ($line in cat .\result.txt){ 
    $length = $line.Length-4
    $arg1 = $line.Substring(0, $length)
    $path = [System.String]::Concat($arg1, ".py")
    New-Item -Path $path -ItemType File
    $pdf = "pdf_reader.py"
    python $pdf $arg1
    $py = "date_finder.py"
    python $py $path
    Remove-Item -Path $path
}

rm .\result.txt

