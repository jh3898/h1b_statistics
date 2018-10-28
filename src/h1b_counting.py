##### Jinting Hang data challenge


def processing_data(infile, key1,key2):
    # input file and two key words to get corresponding column index
    outp = []; dic = {}
    k, tot,n = 0, 0 ,0
    # read file line by line
    for line in [line for line in open(infile, 'r')]: 
        k += 1
        # read each element in a line
        temp = [element.strip('"') for element in line.split(';')]
        if k == 1:
          # read header to get corresponding index to key (SOC & NAME, WORKSITE & STATE)

          n = temp.index(next((s for s in temp if (key1.lower() in s.lower() and key2.lower() in s.lower()))))

          
        else:

            occup = temp[n]

            if temp[2] == 'CERTIFIED':
                if occup in dic:
                    # count the occupation/state number of certified person
                    dic[occup] += 1
                    # total number of certified person

                else:
                    dic[occup] = 1
                tot += 1
    k = 0
    # sort the dictionary in reversed order for the value, alphabetical order for the key,
    # then calculate the percentage, write into output list
    for top_oc, nm_cer in sorted(dic.items(), key = lambda kv :(-kv[1],kv[0])):
        k += 1   ### output only the first 10 rows
        perc = str(round(nm_cer/tot*100,1)) + '%'
        outp.append(top_oc + ';'+ str(nm_cer) + ';' + perc)
        if k >= 9:
            break
    return outp
        
def In_out(infile,outfile1,outfile2):
    ## write into output file 1
    with open(outfile1, 'w+') as file:
        file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        out1= processing_data(infile, 'SOC','NAME')
        for line in [line for line in out1]:  
            file.write(line +'\n')
    ## write into output file 2
    with open(outfile2, 'w+') as file:
        file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        out2 = processing_data(infile, 'WORK','STATE')
        for line in [line for line in out2]:
            file.write(line +'\n')


if __name__ == '__main__':
    # name of input file
    infile = "./input/h1b_input.csv"
    # two output file names
    outfile1 = './output/top_10_occupations.txt'
    outfile2 = './output/top_10_states.txt'
    # run function In_out to read input file and write into out files
    In_out(infile,outfile1,outfile2)
