import sys
import re

def convert_list(input_file, output_file, source_type):
    """
    Convert domain lists to AdguardHome format
    source_type: 'gfw' or 'china'
    """
    with open(input_file, 'r') as f1, open(output_file, 'w') as f2:
        str1 = r'server='
        str2 = r'['
        
        if source_type == 'gfw':
            str3 = r'/127.0.0.1#5353'
            str4 = r'/]tls://1.1.1.1'
        else:  # china
            str3 = r'/114.114.114.114'
            str4 = r'/]tcp://223.6.6.6'
            
        for line in f1:
            t1 = re.sub(str1, str2, line)
            t2 = re.sub(str3, str4, t1)
            f2.write(t2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python domain_list_converter.py <gfw|china> <input_file>")
        sys.exit(1)
        
    source_type = sys.argv[1]
    input_file = sys.argv[2]
    output_file = './gfwlist_AdguardHome.txt' if source_type == 'gfw' else './CNDomains_AdguardHome.txt'
    
    convert_list(input_file, output_file, source_type)
