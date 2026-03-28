import requests
from bs4 import BeautifulSoup

profiles = [
"https://leetcode.com/u/Akanksha_Gupta801/",
"https://leetcode.com/u/Alankratis/",
"https://leetcode.com/u/Ankit_1309/",
"https://leetcode.com/u/arunpra121/",
"https://leetcode.com/u/ASHISH_141/",
"https://leetcode.com/u/Bhagirath772/",
"https://leetcode.com/u/Khusavant/",
"https://leetcode.com/u/DiyaRathor/",
"https://leetcode.com/u/gambhirlairenjam_2004/",
"https://leetcode.com/u/harshityadav9962/",
"https://leetcode.com/u/dRTgtIZRud/",
"https://leetcode.com/u/vrashti_paryani/",
"https://leetcode.com/u/Harsh2706/",
"https://leetcode.com/u/patelmansi7825/",
"https://leetcode.com/u/piyush_Algorithms/",
"https://leetcode.com/u/Jayesh_84/",
"https://leetcode.com/u/rajpa1223/",
"https://leetcode.com/u/Sanket342",
"https://leetcode.com/u/rudra_016/",
"https://leetcode.com/u/G5Y81aJGxf/",
"https://leetcode.com/u/fXEegl1r7O/",
"https://leetcode.com/u/rishumour/",
"https://leetcode.com/u/Rishav9955/",
"https://leetcode.com/u/Wedge_2105/",
"https://leetcode.com/u/itxzz_saanu-09/",
"https://leetcode.com/u/S-hivam_321/",
"https://leetcode.com/u/BRXJFAG2E4/",
"https://leetcode.com/u/solo_officials/",
"https://leetcode.com/u/surya_pratap_1902/",
"https://leetcode.com/u/Bhavya_Thakare/",
"https://leetcode.com/u/Sankirtan_63/",
"http://leetcode.com/u/vxnsh_17/",
"https://leetcode.com/u/Varun94/",
"https://leetcode.com/u/yashbajaj02/",
"https://leetcode.com/u/Leela297/",
"https://leetcode.com/profile/account/",
"https://leetcode.com/u/divvv_codex/",
"https://leetcode.com/u/Manishkachinoria11/",
"https://leetcode.com/u/Priyani_nuthra/",
"https://leet.com/u/_verma_rajat_/",
"https://leetcode.com/u/RanaDhruv13/",
"https://leetcode.com/u/krutarth2006/",
"https://leetcode.com/u/Janki_1905/",
"https://leetcode.com/u/Mahi4114",
"https://leetcode.com/u/Prem9771",
"https://leetcode.com/u/rahulsain1501/",
"https://leetcode.com/u/abhisheksingh45/",
"https://leetcode.com/u/Nice_AK/",
"http://leetcode.com/u/mansimanvani/",
"https://leetcode.com/u/Dakshp725/",
"https://leetcode.com/u/Patil_Sayali/",
"https://leetcode.com/u/vinay3132006/",
"https://leetcode.com/u/KrrishR05/",
"https://leetcode.com/u/KhushiTcode/",
"https://leetcode.com/u/aagam_1910/",
"https://leetcode.com/u/Himanhujangir01/"
]

def get_solved(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return 0
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text()
        import re
        match = re.search(r"Solved\s+(\d+)", text)
        if match:
            return int(match.group(1))
        else:
            return 0
    except:
        return 0

results = []

for url in profiles:
    solved = get_solved(url)
    results.append((url, solved))
    print(url, "->", solved)

# Save to CSV
import csv
with open("leetcode_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Profile", "Problems Solved"])
    for r in results:
        writer.writerow(r)

print("\nCSV file generated: leetcode_results.csv")
