<?php

// Load XML documentation
$xml = new DOMDocument();
$xml->load('users.xml');

// create XML Object 
$xpath = new DOMXPath($xml);


//
$username = 'admin';
$password = 'admin';

//XPATH Query 
$query = "//user";
$entries = $xpath->query($query);

//Print Node Elements.
if ($entries->length > 0){
    foreach ($entries as $entry) {
    
        // Extracting Nofr d
        echo "Node Name: " . $entry->nodeName . "\n";
        
        // Print child Node Elements 
        foreach ($entry->childNodes as $child) {
            if ($child->nodeType == XML_ELEMENT_NODE) {
                echo $child->nodeName . ": " . $child->nodeValue . "\n";
            }
        }
    }
}

?>