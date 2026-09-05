$ErrorActionPreference = 'Stop'
$dir = 'C:\Users\jgtit\AppData\Local\Temp\claude\C--Users-jgtit-claude\b91e0deb-2ccd-4ec3-aef4-6352ae05fe8e\scratchpad\govdocx'
$docx = Join-Path $dir 'draft.docx'
$pdf  = Join-Path $dir 'draft.pdf'
if (Test-Path $pdf) { Remove-Item $pdf -Force }
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    $doc = $word.Documents.Open($docx, $false, $true)
    $pages = $doc.ComputeStatistics(2)   # wdStatisticPages
    $doc.ExportAsFixedFormat($pdf, 17)    # wdExportFormatPDF
    $doc.Close(0)
    Write-Output "PAGES=$pages"
    Write-Output "PDF=$pdf"
} finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}
