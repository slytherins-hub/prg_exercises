# CVIČENÍ 1: PRVNÍ KROKY S PYTHONEM

Algoritmizace a programování

## CÍL 1: INSTALACE A PŘÍPRAVA PROSTŘEDÍ (UV)

Pro správu našich projektů, knihoven a verzí Pythonu budeme používat nástroj `uv`. Tento nástroj nám výrazně zjednoduší práci s tzv. **virtuálními prostředími**.

> **Proč virtuální prostředí?**
> Každý projekt může potřebovat jiné verze knihoven. Virtuální prostředí izoluje projekty od sebe – jako mít samostatný pracovní stůl pro každý projekt. Změny v jednom projektu neovlivní ostatní. Bez toho by aktualizace knihovny pro jeden projekt mohla rozbít všechny ostatní projekty.

### 1.1 Založení projektu a virtuálního prostředí

**Krok 1: Vytvoření složky pro projekt**

Nejprve si vytvoříme složku pro naše cvičení:

1. Otevřete **Průzkumník souborů** (File Explorer)
2. Přejděte na **Plochu** (Desktop)
3. Klikněte pravým tlačítkem do volného prostoru → **Nový** → **Složka**
4. Pojmenujte ji například `exercise01`

**Krok 2: Otevření PowerShellu ve složce**

Nyní musíme otevřít terminál (PowerShell) v této složce:

1. Otevřete složku `exercise01` (dvojklik)
2. Klikněte pravým tlačítkem do volného prostoru uvnitř složky
3. Zvolte **"Otevřít v terminálu"** (Open in Terminal) nebo **"Open in Windows Terminal"**

Otevře se okno PowerShellu s cestou k vaší složce (např. `C:\Users\Jméno\Desktop\exercise01>`).

**Krok 3: Instalace `uv`**

Nejprve musíme nástroj `uv` nainstalovat. Otevřete příkazovou řádku (Terminal) a spusťte následující příkaz (dle vašeho operačního systému):

> ** Instalace jen jednou:**
> Instalaci `uv` stačí provést **pouze jednou na každém počítači**. Pokud už máte `uv` nainstalovaný, přeskočte na sekci 1.2.
>
> Pokud se přesunete na jiný školní počítač, budete muset `uv` nainstalovat znovu.

**Windows** (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Po instalaci restartujte terminál a ověřte, že `uv` funguje příkazem:
```bash
uv --version
```

**Krok 4: Inicializace projektu**

V terminálu (PowerShellu) zadejte příkaz `uv init`. Tento příkaz vytvoří základní strukturu projektu:

Zadej do PowerShellu:

```bash
uv init
```

Po spuštění uvidíte, že v adresáři vznikly nové soubory, zejména:

- `main.py` – hlavní soubor s ukázkovým kódem
- `pyproject.toml` – konfigurační soubor projektu

**Krok 5: Vytvoření virtuálního prostředí**

Nyní vytvoříme virtuální prostředí pomocí příkazu `uv sync`:

Zadej do PowerShellu:

```bash
uv sync
```

Tento příkaz:

- Vytvoří složku `.venv` s virtuálním prostředím
- Nainstaluje Python (pokud není k dispozici)
- Připraví vše potřebné pro běh vašich programů

> ** Zobrazení přípony souborů a skrytých souborů:**
>
> Pro programování je důležité vidět **přípony souborů** (`.py`, `.txt`) a **skryté soubory** (např. složku `.venv`).
>
> **Jak to zapnout ve Windows:**
>
> 1. Otevřete **Průzkumník souborů** (File Explorer)
> 2. Klikněte na záložku **Zobrazení** (View) nahoře
> 3. Zaškrtněte:
>    - **Přípony názvů souborů** (File name extensions)
>    - **Skryté položky** (Hidden items)
>
> **Alternativně (Windows 11):**
> - V Průzkumníku souborů klikněte na **⋯ (tři tečky)** → **Možnosti** → **Zobrazení**
> - V seznamu najděte a **odškrtněte**: "Skrýt přípony souborů známých typů"
> - Najděte a **zaškrtněte**: "Zobrazit skryté soubory, složky a jednotky"
>
> **Proč je to důležité?**
> - Uvidíte, zda je soubor opravdu `.py` (a ne `.py.txt`)
> - Uvidíte složku `.venv` s virtuálním prostředím
> - Poznáte konfigurační soubory jako `.gitignore`

### 1.2 Práce v PyCharmu (konfigurace projektu)

Abychom mohli pohodlně psát kód a spouštět programy, otevřeme naši složku v prostředí PyCharm.

> **📥 Instalace PyCharm:**
> - **Na školních počítačích** je PyCharm již nainstalovaný
> - **Doma si PyCharm stáhněte** z [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/) a nainstalujte (vyberte správnou verzi podle vašeho operačního systému)

1. Spusťte **PyCharm**.
2. Na úvodní obrazovce zvolte **Open...** (nebo v menu **File > Open...**).
3. Najděte a vyberte složku `exercise01`, kterou jsme připravili, a potvrďte **OK**.

> ** Co je to "projekt" v PyCharmu?**
>
> PyCharm může při otevírání složky nabídnout vytvoření "projektu" (`.idea` složka s nastavením). Projekt v PyCharmu ukládá různá nastavení – jaký Python interpreter používáte, jaké máte otevřené soubory, kde máte záložky atd.
>
> **Pro tento kurz to nepotřebujete** – můžete klidně otevřít složku "bez projektu" (This Window / Trust Project). Nastavení interpreteru si PyCharm zapamatuje i bez projektu. Pokud se projekt vytvoří, nic se nestane, `.idea` složku můžete ignorovat.

4. **Nastavení interpretu (Pythonu):**

 * PyCharm by měl automaticky detekovat složku `.venv`.
 * Zkontrolujte vpravo dole v liště, zda vidíte verzi Pythonu (např. `Python 3.13 (exercise01)`).
 * Pokud vidíte `<No interpreter>`, klikněte na něj → **Add New Interpreter** → **Add Local Interpreter...** → **Virtual Environment** ().
 * Zvolte **Existing** a nalistujte cestu k `python.exe` ve vaší složce: `exercise01/.venv/Scripts/python.exe` (na Windows) nebo `exercise01/.venv/bin/python` (macOS/Linux).
 * (V novějším PyCharmu zvolte **Existing**, Type: **uv**, Path to uv: `C:\Users\<login>\.local\bin\uv.exe` a nalistujte cestu k `python.exe` ve vaší složce: `exercise01/.venv/Scripts/python.exe` (na Windows) nebo `exercise01/.venv/bin/python` (macOS/Linux).)
Nyní PyCharm používá prostředí, které spravuje `uv`.

5. Vypněte doplňování řádků:

 * Otevřete nastavení **File > Settings...**.
 * V levém sloupci rozklikněte možnost **Editor > General > Inline Completion**.
 * Zrušte zaškrtnutí možnosti **Enable local Full Line completion suggestions**.

### 1.3 VUT disk
Ve školním počítači máte k dispozici osobní disk, tzv. VUT disk, obvykle namapovaný pod označením `V:`. Tento disk je soukromý a k jeho obsahu lze přistupovat pouze po zadání přihlašovacích údajů. To probíhá automaticky při přihlášení v počítačové učebně.

VUT disk je možné používat pro ukládání souborů ze cvičení tak, abyste k nim měli přístup i z domova. Pro přístup k tomuto disku mimo učebnu je nutné využít VPN. Podrobný návod k VUT disku najdete v Intraportálu [https://www.vut.cz/intra/vutdisk](https://www.vut.cz/intra/vutdisk).

---

