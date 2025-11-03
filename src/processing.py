def clean_rows(rows: list[dict]) -> list[dict]:
    """Boş veya geçersiz yaş içeren satırları kaldır, verileri temizle"""
    cleaned = []
    for r in rows:
        name = r.get("name", "").strip()
        city = r.get("city", "").strip()
        age = r.get("age", "").strip()

        if not age.isdigit():
            continue 

        cleaned.append({
            "name": name,
            "age": int(age),
            "city": city
        })

    return cleaned


def stats(rows: list[dict]) -> dict:
    if not rows:
        return {"count": 0, "avg_age": 0, "by_city": {}}

    ages = [r["age"] for r in rows]
    by_city = {}
    for r in rows:
        by_city[r["city"]] = by_city.get(r["city"], 0) + 1

    return {
        "count": len(rows),
        "avg_age": round(sum(ages) / len(ages), 2),
        "by_city": by_city
    }


def build_report(st: dict) -> str:
    lines = [
        "Rapor",
        "",
        f"Geçerli kayıt sayısı: {st['count']}",
        f"Ortalama yaş: {st['avg_age']}",
        "Şehir dağılımı:",
    ]
    for c, n in st["by_city"].items():
        lines.append(f"  {c}: {n}")
    return "\n".join(lines) + "\n"
