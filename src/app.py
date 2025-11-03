from operations import read_csv, write_json, write_text
from processing import clean_rows, stats, build_report

def main():
    read_doc = "./data/people.csv"
    cleaned_json = "./data/cleaned.json"
    stats_json = "./data/stats.json"
    report_txt = "./data/report.txt"

    rows = read_csv(read_doc)
    rows = clean_rows(rows)
    st = stats(rows)

    write_json(cleaned_json, rows)
    write_json(stats_json, st)
    write_text(report_txt, build_report(st))

    print("İşlem tamamlandı!")

if __name__ == "__main__":
    main()
