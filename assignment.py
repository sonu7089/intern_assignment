def convert(content):
    ans = ""
    list = []
    #find position of text after how many ',' in this case we are assuming at 9th but ideally should be done dynamically
    cnt = 0
    prefixOfD = ""
    posOfText = 9
    for line in content.split('\n'):
        if cnt != 0:
            cnt -= 1
            continue
        if line.startswith('Dialogue:'):
            x = line.split(',')
            pod = ""
            for i in range(len(x)):
                if i != 9:
                    pod += x[i] + ","
            prefixOfD = pod
            str = x[posOfText].split(' ')
            cnt = len(str)
            tmpStr = ""
            for s in str:
                if s.startswith('{'):
                    tmpStr += s[5:len(s) - 4] + " "
                else:
                    tmpStr += s +" "
            list.append(tmpStr)
        else:
            ans += line+"\n"
        
    
    prefixOfPrev = prefixOfD.replace('Default', 'P')
    prefixOfNext = prefixOfD.replace('Default', 'F')

    cur = 0
    cnt = 0
    flag = 0
    for line in content.split('\n'):
        if line.startswith('Dialogue:'):
            if cnt == 0 and flag == 0:
                cnt = len(line.split(',')[9].split(' ')) - 1
                flag = 1
            elif cnt == 0:
                cnt = len(line.split(',')[9].split(' ')) - 1
                cur += 1
            else:
                cnt -= 1
            if cur == 0:
                ans += prefixOfPrev+"...\n"
            else:
                ans += prefixOfNext+ list[cur-1]+"\n"
            ans += line+"\n"
            if cur >= len(list) - 1:
                ans += prefixOfNext+"...\n"
            else:
                ans += prefixOfNext+ list[cur+1]+"\n" 
            
             
            ans += "\n"
    return ans

if __name__ == "__main__":
    input_file = "input_subtitles.ass"
    try:
        with open(input_file, 'r') as file:
            content = file.read()

            f = open("output_subtitles.ass", "x")
            f.write(convert(content))
            f.close()
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An error occurred while reading the file.")
