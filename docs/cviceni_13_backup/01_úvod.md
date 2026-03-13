# CVIČENÍ 13: OOP

Algoritmizace a programování

## ÚVOD

Doteď jsi pracoval hlavně s funkcemi, seznamy, slovníky a samostatnými proměnnými. To je pro spoustu úloh úplně v pohodě. Jakmile ale začneš pracovat se složitějšími daty a chceš nad nimi dělat opakované operace, začne být výhodné držet data a operace nad nimi pohromadě.

Právě k tomu slouží **objektově orientované programování**. Místo toho, abys měl zvlášť data, zvlášť metadata a zvlášť několik funkcí kolem nich, můžeš mít jeden objekt, který to všechno nese společně.

V tomhle cvičení budeme mluvit o OOP obecně, ale příklady budeme brát z biomedicíny a bioinformatiky. Budeme pracovat s `numpy` poli a nad nimi si ukážeme jednoduché třídy.

### Co se v tomto cvičení naučíte?

1. Proč dává smysl balit vědecká data do objektů.
2. Jak navrhnout třídu s atributy a metodami.
3. Jak třídu rozšiřovat postupně – přidávat metody a speciální metody jako `__str__`.
4. Jak pracovat se seznamem objektů a dělat nad nimi analýzu.
5. Co je dědičnost, kdy ji použít a jak ji napsat.

### Jak je cvičení postavené

Po celé cvičení pracujeme s jednou třídou – **biomedicínský signál**. Začneme od základů, postupně ji rozšíříme, vyzkoušíme práci s více objekty najednou a nakonec si ukážeme dědičnost: jak ze společného základu odvodit specializované třídy pro EKG, dech nebo jiné typy měření.

Konkrétní příklady v kódu jsou z oblasti biomedicíny: signály, pacienti, měření. Principy jsou ale obecné – úplně stejně bys navrhoval třídu pro fyzikální experiment, genomická data nebo cokoliv jiného.

> **💡 Tip:** Tohle cvičení není o tom, naučit se všechno o OOP naráz. Cílem je pochopit základní princip: objekt drží data a zároveň umí nabídnout operace, které k těm datům patří – a vidět, jak se to princip škáluje od jedné třídy přes seznam objektů až po hierarchii dědičných tříd.

---