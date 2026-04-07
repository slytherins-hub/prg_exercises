# CVIČENÍ 9: ZÁKLADY GIT A GITHUB

Algoritmizace a programování

## CÍL 3: SPOLUPRÁCE – GITHUB

Při práci na společném projektu je klíčové, aby každý člen týmu měl přístup k práci ostatních. Vyzkoušíme si, 
jak přistupovat ke vzdálenému repozitáři, jak z něj získat aktuální stav projektu i jak do něj přispět vlastními změnami.

---

### 3.1 Klonování repozitáře

Jednou ze služeb poskytujících možnost nahrání gitového repozitáře a sdílení s ostatními je **GitHub**. Při práci
na domácích úkolech pracuješ se vzdáleným repozitářem, který vlastníš ty. Teď si vyzkoušíme práci s repozitářem,
který založil někdo jiný.

V příkazové řádce se přepni **mimo složku**, kde jsme doteď pracovali, a zadej příkaz `git clone` s odkazem na repozitář
(adresa je na e-learningu):

```bash
git clone https://github.com/ucet-cviciciho/nazev-repozitare
```

Díky tomuto příkazu se vytvoří nová složka s obsahem repozitáře. Na obsah se můžeš podívat i v prohlížeči po zadání
stejného odkazu.

> **📘 Co je `git clone`?**
>
> `git clone` vytvoří lokální kopii vzdáleného repozitáře včetně celé jeho historie. Na rozdíl od stahování ZIP souboru
> získáš i všechny větve a revize.

---

### 3.2 Zapojení do projektu

#### ÚKOL: Přidání souboru do naklonovaného repozitáře

1. Přepni se do naklonované složky a zkontroluj historii repozitáře (např. pomocí `gitk --all` nebo `git log --oneline`).
2. V pracovním adresáři vytvoř prázdný textový soubor a ulož ho pod svým jménem (`jmeno_prijmeni.txt`). Nepoužívej diakritiku.
3. Vytvoř novou revizi:

```bash
git add jmeno_prijmeni.txt
git commit -m "Add attendance file"
```

---

### 3.3 Fork a pull request

Teď zbývá změny začlenit do původního repozitáře. Původní majitel si nepřeje, aby mu kdokoliv mohl zasahovat do práce. Proto musíš:

1. Nahrát změny do **vlastního** repozitáře.
2. Dát majiteli vědět formou **žádosti o začlenění** (**pull request**).
3. Majitel rozhodne, zda změny začlení nebo ne.

![Fork workflow](../assets/cviceni_09/08_github_fork_workflow.png)

**Vytvoření forku:**

1. Otevři si v prohlížeči GitHub a přihlas se.
2. Otevři odkaz na repozitář, který jsme klonovali.
3. Vpravo nahoře najdeš tlačítko **Fork** – klikni na něj.
4. Teď máš vlastní kopii repozitáře.

---

### 3.4 Propojení se vzdáleným repozitářem

Podívej se na adresy vzdálených repozitářů, které si Git pamatuje:

```bash
git remote -v
```

!!! output "Výstup"
    ```text
    origin  https://github.com/ucet-cviciciho/nazev-repozitare (fetch)
    origin  https://github.com/ucet-cviciciho/nazev-repozitare (push)
    ```

Pod zkratkou `origin` vidíš adresu původního vzdáleného repozitáře. Vytvoř si zkratku k **tvému** vzdálenému repozitáři:

```bash
git remote add muj_fork https://github.com/tvuj-ucet/nazev-repozitare
```

```bash
git remote -v
```

!!! output "Výstup"
    ```text
    origin    https://github.com/jmeno/prezencka (fetch)
    origin    https://github.com/jmeno/prezencka (push)
    muj_fork  https://github.com/tvuj-ucet/nazev-repozitare (fetch)
    muj_fork  https://github.com/tvuj-ucet/nazev-repozitare (push)
    ```

---

### 3.5 Nahrání změn na GitHub

Pošli změny na svůj vzdálený repozitář:

```bash
git push muj_fork main
```

V prohlížeči zkontroluj, že nahrání proběhlo.

---

### 3.6 Vytvoření pull requestu

Na stránce tvého vzdáleného repozitáře se nahoře objeví možnost **Contribute** a po rozkliknutí **Open pull request**.
Otevři nový pull request, zkontroluj popisek změny a potvrď ho.

> **📘 Co je pull request?**
>
> Pull request je žádost o začlenění tvých změn do původního repozitáře. Před začleněním obvykle probíhá 
> **kontrola kódu** (**code review**) – majitel může mít připomínky a vyžádat si další úpravy, nebo změny rovnou schválí.

Další revize můžeš do pull requestu přidat opakováním:

```bash
git add jmeno_prijmeni.txt
git commit -m "Update attendance file"
git push muj_fork main
```

Pokud jsou změny v pořádku, majitel provede jejich začlenění (**Merge pull request**).

---

### 3.7 Aktualizace lokální kopie

Abys vždy pracoval/a na nejnovější verzi, je potřeba aktualizovat lokální kopii:

```bash
git pull origin main
```

Pomocí `git status` ověř stav repozitáře a pomocí `gitk --all` nebo `git log --oneline` zkontroluj, jak se projekt posunul.

---

### 3.8 Komplexní workflow s větvemi

#### ÚKOL 7: Větev, push a pull request

1. V repozitáři prezencka vytvoř novou větev:

    ```bash
    git branch nazev_vetve
    ```

2. Přepni se do nově vytvořené větve:

    ```bash
    git switch nazev_vetve
    ```

3. V souboru se svým jménem proveď potřebné změny (např. doplň, jakou máš dnes náladu).
4. Vytvoř novou revizi.
5. Pošli změny do svého vzdáleného repozitáře:

    ```bash
    git push muj_fork nazev_vetve
    ```

6. Na GitHubu vytvoř **pull request**.

**Po začlenění tvých změn:**

7. Přepni se zpět na hlavní větev:

    ```bash
    git switch main
    ```

8. Stáhni aktuální verzi repozitáře:

    ```bash
    git pull origin main
    ```

9. Smaž větev, na které jsou začleněné změny:

    ```bash
    git branch -d nazev_vetve
    ```
