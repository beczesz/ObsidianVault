const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  HeadingLevel, BorderStyle, PageBreak,
  Header, Footer, PageNumber,
  TabStopType, TabStopPosition,
  LevelFormat
} = require('docx');

// Helper: bekezdés készítése
function p(text, opts = {}) {
  return new Paragraph({
    children: [new TextRun({ text, bold: opts.bold, italics: opts.italics, size: opts.size || 22 })],
    alignment: opts.align || AlignmentType.JUSTIFIED,
    spacing: { after: opts.after || 100 },
    ...opts.paragraph
  });
}

// Helper: title (bold center)
function title(text, opts = {}) {
  return new Paragraph({
    children: [new TextRun({ text, bold: true, size: opts.size || 28 })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 200, after: 200 }
  });
}

// Helper: heading 2 (article)
function h2(text) {
  return new Paragraph({
    children: [new TextRun({ text, bold: true, size: 24 })],
    alignment: AlignmentType.LEFT,
    spacing: { before: 240, after: 120 }
  });
}

// Helper: list item (bullet)
function li(text, level = 0) {
  return new Paragraph({
    numbering: { reference: 'bullets', level },
    children: [new TextRun({ text, size: 22 })],
    spacing: { after: 60 }
  });
}

// Helper: numbered (a/b/c)
function pAlpha(letter, text) {
  return new Paragraph({
    children: [
      new TextRun({ text: `${letter}) `, bold: true, size: 22 }),
      new TextRun({ text, size: 22 })
    ],
    spacing: { after: 80 },
    indent: { left: 360 },
    alignment: AlignmentType.JUSTIFIED
  });
}

const doc = new Document({
  creator: "Notar Public Andrei Munteanu",
  title: "Contract de închiriere - TransOffice Trade SRL",
  styles: {
    default: {
      document: { run: { font: "Times New Roman", size: 22 } }
    }
  },
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [
          { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
        ]
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1134, right: 1134, bottom: 1134, left: 1134 } // 2 cm minden oldal
      }
    },
    headers: {
      default: new Header({ children: [
        new Paragraph({
          children: [new TextRun({ text: "CONTRACT DE ÎNCHIRIERE — Nr. 47/26.04.2018", size: 16, color: "555555" })],
          alignment: AlignmentType.RIGHT
        })
      ]})
    },
    footers: {
      default: new Footer({ children: [
        new Paragraph({
          children: [
            new TextRun({ text: "Pagina ", size: 16, color: "555555" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "555555" }),
            new TextRun({ text: " din ", size: 16, color: "555555" }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: "555555" }),
          ],
          alignment: AlignmentType.CENTER
        })
      ]})
    },
    children: [
      // ============ HEADER / TITLU ============
      title("CONTRACT DE ÎNCHIRIERE", { size: 32 }),
      title("PRIVIND BUNUL IMOBIL CU DESTINAȚIA DE SPAȚIU COMERCIAL ȘI DEPOZIT", { size: 24 }),
      
      new Paragraph({
        children: [new TextRun({ text: "Nr. 47 / 26.04.2018", bold: true, size: 22 })],
        alignment: AlignmentType.CENTER,
        spacing: { before: 100, after: 240 }
      }),

      // ============ I. PĂRȚILE CONTRACTANTE ============
      h2("I. PĂRȚILE CONTRACTANTE"),
      
      p("Prezentul contract de închiriere se încheie astăzi, 26 aprilie 2018, în Odorheiu Secuiesc, județul Harghita, între:"),
      
      p("1. BÉLA IOSIF, cetățean român, domiciliat în Odorheiu Secuiesc, str. Tamási Áron nr. 14, județul Harghita, identificat prin C.I. seria HR nr. 287456, eliberată de SPCLEP Odorheiu Secuiesc la data de 12.03.2015, CNP 1581012191234, în calitate de proprietar al imobilului care face obiectul prezentului contract, denumit în continuare „LOCATOR\";", { paragraph: { spacing: { after: 120 } } }),
      
      p("ȘI", { align: AlignmentType.CENTER, paragraph: { spacing: { before: 80, after: 80 } } }),
      
      p("2. SOCIETATEA TRANSOFFICE TRADE S.R.L., cu sediul social în Odorheiu Secuiesc, str. Calea Băieșenilor nr. 22, județul Harghita, înregistrată la Oficiul Registrului Comerțului de pe lângă Tribunalul Harghita sub nr. J19/421/2003, cod unic de înregistrare 15847291, atribut fiscal RO, având cont bancar deschis la Banca Transilvania, Sucursala Odorheiu Secuiesc, IBAN RO47BTRLRONCRT0287654321, reprezentată legal prin domnul KOVÁCS ISTVÁN, în calitate de administrator unic, identificat prin C.I. seria HR nr. 145872, CNP 1620315191234, în calitate de chiriaș al imobilului care face obiectul prezentului contract, denumit în continuare „LOCATAR\".", { paragraph: { spacing: { after: 200 } } }),
      
      p("Cele două părți denumite în mod individual „PARTEA\" și colectiv „PĂRȚILE\", au convenit încheierea prezentului contract de închiriere, cu respectarea prevederilor art. 1777 - 1850 din Codul Civil al României, în următoarele condiții:"),
      
      // ============ II. OBIECTUL CONTRACTULUI ============
      h2("II. OBIECTUL CONTRACTULUI"),
      
      p("Art. 1. Obiectul prezentului contract îl constituie închirierea de către LOCATOR către LOCATAR, în schimbul plății unei chirii lunare, a următorului imobil:", { paragraph: { spacing: { after: 80 } } }),
      
      pAlpha("a", "Spațiu de depozit cu suprafața utilă de 412 m², situat la parterul construcției C1, având destinația „depozit produse industriale\";"),
      pAlpha("b", "Spațiu administrativ cu suprafața utilă de 78 m², situat la etajul 1 al construcției C1, având destinația „birouri și sală de ședințe\";"),
      pAlpha("c", "Suprafață exterioară pavată de 245 m², destinată parcării și manevrelor logistice, parte integrantă a parcelei cadastrale."),
      
      p("Art. 2. Imobilul închiriat este situat în Odorheiu Secuiesc, str. Calea Băieșenilor nr. 22, județul Harghita, având numărul cadastral 51487 și carte funciară nr. 51487/N a UAT Odorheiu Secuiesc, fiind în întregime proprietatea privată a LOCATORULUI conform contractului de vânzare-cumpărare autentificat sub nr. 1832/15.07.1998 la BNP Andrei Munteanu, Odorheiu Secuiesc."),
      
      p("Art. 3. Suprafața totală închiriată este de 735 m² (șapte sute treizeci și cinci metri pătrați), conform planului de amplasament și delimitare anexat ca Anexa nr. 1 la prezentul contract."),
      
      p("Art. 4. Imobilul închiriat se predă LOCATARULUI în starea tehnică și funcțională în care se află la data semnării prezentului contract, conform procesului-verbal de predare-primire ce constituie Anexa nr. 2."),
      
      // ============ III. DURATA CONTRACTULUI ============
      h2("III. DURATA CONTRACTULUI"),
      
      p("Art. 5. Prezentul contract se încheie pe o perioadă de 10 (zece) ani, începând cu data de 1 mai 2018 și expirând la data de 30 aprilie 2028."),
      
      p("Art. 6. La expirarea perioadei prevăzute la art. 5, prezentul contract poate fi prelungit prin acordul scris al ambelor PĂRȚI, exprimat printr-un act adițional. Dacă niciuna dintre PĂRȚI nu notifică în scris cealaltă PARTE, cu cel puțin 90 de zile calendaristice înainte de expirarea contractului, intenția de a nu prelungi contractul, acesta se prelungește automat pentru o perioadă de 1 (un) an, cu posibilitatea unor noi prelungiri succesive în aceleași condiții."),
      
      p("Art. 7. Prezentul contract va fi înregistrat de LOCATOR la organul fiscal competent (ANAF Harghita) în termen de 30 zile de la semnare, conform prevederilor art. 1781 Cod Civil și ale Codului Fiscal."),
      
      // ============ IV. CHIRIA ============
      h2("IV. CHIRIA ȘI MODALITATEA DE PLATĂ"),
      
      p("Art. 8. Cuantumul chiriei lunare este stabilit de comun acord la suma de 4.850 LEI (patru mii opt sute cincizeci lei), echivalentul a aproximativ 1.040 EUR la cursul BNR din data semnării prezentului contract."),
      
      p("Art. 9. Chiria se plătește lunar, în avans, până la data de 5 (cinci) a fiecărei luni pentru luna în curs, prin virament bancar în contul LOCATORULUI: RO62BCRT00415247869521 deschis la Banca Comercială Română, Sucursala Odorheiu Secuiesc."),
      
      p("Art. 10. Cuantumul chiriei se actualizează automat în fiecare an, începând cu data de 1 ianuarie a anului calendaristic următor, cu indicele prețurilor de consum (IPC) comunicat de Institutul Național de Statistică pentru anul precedent. LOCATORUL va comunica LOCATARULUI noul cuantum până la 15 ianuarie a fiecărui an, prin notificare scrisă."),
      
      p("Art. 11. La data semnării prezentului contract, LOCATARUL achită LOCATORULUI o garanție de bună execuție în cuantum de 9.700 LEI (echivalentul a 2 luni de chirie), care se restituie la încetarea contractului, după deducerea eventualelor sume datorate, în termen de 30 zile de la predarea imobilului."),
      
      p("Art. 12. Întârzierea la plata chiriei mai mare de 10 zile calendaristice atrage o penalitate de 0,1% pe zi de întârziere din suma datorată, dar nu mai mult de cuantumul total al chiriei restante."),
      
      // ============ V. OBLIGAȚIILE LOCATORULUI ============
      h2("V. OBLIGAȚIILE LOCATORULUI"),
      
      p("Art. 13. LOCATORUL se obligă:", { paragraph: { spacing: { after: 80 } } }),
      pAlpha("a", "să predea LOCATARULUI imobilul închiriat în stare corespunzătoare folosinței prevăzute în contract, conform Anexei nr. 2 (proces-verbal de predare-primire);"),
      pAlpha("b", "să asigure folosința pașnică și utilă a imobilului pe toată durata contractului;"),
      pAlpha("c", "să efectueze, pe cheltuiala sa, reparațiile capitale și de natură structurală a imobilului (acoperiș, pereți portanți, instalații generale aflate sub plinta exterioară);"),
      pAlpha("d", "să plătească impozitele și taxele aferente proprietății (impozit pe clădiri, impozit pe teren) către bugetul local;"),
      pAlpha("e", "să comunice LOCATARULUI orice modificare survenită în situația juridică a imobilului (vânzare, ipotecă, sechestru, succesiune) în termen de 15 zile calendaristice de la data producerii."),
      
      // ============ VI. OBLIGAȚIILE LOCATARULUI ============
      h2("VI. OBLIGAȚIILE LOCATARULUI"),
      
      p("Art. 14. LOCATARUL se obligă:", { paragraph: { spacing: { after: 80 } } }),
      pAlpha("a", "să folosească imobilul exclusiv conform destinației stabilite la art. 1 (depozit, birouri, parcare comercială);"),
      pAlpha("b", "să plătească chiria și toate utilitățile (energie electrică, apă-canal, gaz, salubritate, internet) în termenele convenite;"),
      pAlpha("c", "să întrețină imobilul în stare bună de funcționare și să efectueze, pe cheltuiala sa, reparațiile curente (zugrăveli, schimbări de becuri, întreținerea instalațiilor sanitare interioare, mici intervenții electrice);"),
      pAlpha("d", "să nu subînchirieze imobilul sau să nu cedeze contractul unui terț fără acordul scris și prealabil al LOCATORULUI;"),
      pAlpha("e", "să suporte costul asigurării de tip „toate riscurile\" pentru bunurile sale aflate în spațiu, precum și asigurarea de răspundere civilă față de terți;"),
      pAlpha("f", "să respecte normele de prevenire a incendiilor (P.S.I.), de sănătate și securitate în muncă (S.S.M.), precum și normele de protecție a mediului aplicabile activității desfășurate;"),
      pAlpha("g", "să predea imobilul la încetarea contractului în stare similară cu cea de la preluare, mai puțin uzura normală."),
      
      // ============ VII. ÎMBUNĂTĂȚIRI ȘI MODIFICĂRI ============
      h2("VII. ÎMBUNĂTĂȚIRI, MODIFICĂRI ȘI INVESTIȚII"),
      
      p("Art. 15. LOCATARUL poate efectua îmbunătățiri și modificări în imobilul închiriat numai cu acordul scris și prealabil al LOCATORULUI. Solicitarea LOCATARULUI și răspunsul LOCATORULUI se transmit în formă scrisă, prin email sau scrisoare recomandată cu confirmare de primire."),
      
      p("Art. 16. Bunurile mobile și echipamentele aduse de LOCATAR în imobil (mobilier, echipamente IT, rafturi, utilaje, vehicule, sisteme de încărcare electrică ori alte instalații demontabile) rămân proprietatea exclusivă a LOCATARULUI și pot fi ridicate la încetarea contractului, conform principiului dreptului de retragere a bunurilor mobile prevăzut de art. 1825 Cod Civil."),
      
      p("Art. 17. Lucrările cu caracter permanent realizate de LOCATAR (precum modificări structurale ale clădirii, finisaje încastrate, instalații integrate în structura imobilului), efectuate cu acordul LOCATORULUI, rămân proprietatea LOCATORULUI la încetarea contractului, fără obligația de despăgubire, sub rezerva aplicării art. 1823 Cod Civil."),
      
      p("Art. 18. LOCATARUL este obligat să restabilească starea inițială a imobilului dacă efectuează modificări fără acordul scris al LOCATORULUI sau dacă LOCATORUL solicită expres acest lucru la încetarea contractului."),
      
      // ============ VIII. ÎNCETAREA CONTRACTULUI ============
      h2("VIII. ÎNCETAREA CONTRACTULUI"),
      
      p("Art. 19. Prezentul contract încetează în următoarele situații:", { paragraph: { spacing: { after: 80 } } }),
      pAlpha("a", "prin expirarea termenului prevăzut la art. 5, dacă PĂRȚILE nu convin prelungirea conform art. 6;"),
      pAlpha("b", "prin acordul scris al ambelor PĂRȚI, înainte de termen;"),
      pAlpha("c", "prin reziliere unilaterală din partea LOCATORULUI, în caz de neplată a chiriei pe o perioadă de cel puțin 60 zile calendaristice consecutive sau în caz de încălcare gravă a obligațiilor LOCATARULUI prevăzute la art. 14;"),
      pAlpha("d", "prin reziliere unilaterală din partea LOCATARULUI, cu un preaviz scris de 90 zile calendaristice, în caz de imposibilitate de folosire a imobilului din motive imputabile LOCATORULUI;"),
      pAlpha("e", "prin pieirea totală a imobilului din cauze de forță majoră (incendiu, cutremur, inundație) — în acest caz contractul încetează de drept, fără despăgubiri reciproce;"),
      pAlpha("f", "în caz de înstrăinare a imobilului către un terț, conform art. 21 de mai jos."),
      
      p("Art. 20. La încetarea contractului, LOCATARUL este obligat să predea imobilul LOCATORULUI în termen de 15 zile calendaristice, în baza unui proces-verbal de predare-primire."),
      
      // ============ IX. CESIUNEA ȘI ÎNSTRĂINAREA ============
      h2("IX. CESIUNEA ȘI ÎNSTRĂINAREA IMOBILULUI"),
      
      p("Art. 21. În cazul în care LOCATORUL înstrăinează imobilul către un terț pe perioada de valabilitate a prezentului contract, dispozițiile art. 1811 Cod Civil se aplică în întregime, respectiv noul proprietar este obligat să respecte contractul de închiriere până la expirarea sa, sub condiția ca prezentul contract să fi fost înregistrat la organul fiscal sau în cartea funciară conform art. 7."),
      
      p("Art. 22. LOCATORUL se obligă să notifice LOCATARULUI orice intenție de înstrăinare a imobilului cu cel puțin 60 zile calendaristice înainte de încheierea actului de înstrăinare, în vederea exercitării unui eventual drept de preempțiune al LOCATARULUI, dacă acesta este interesat."),
      
      // ============ X. FORȚA MAJORĂ ============
      h2("X. FORȚA MAJORĂ"),
      
      p("Art. 23. PĂRȚILE sunt exonerate de răspundere pentru neexecutarea sau executarea necorespunzătoare a obligațiilor contractuale, dacă aceasta se datorează unui caz de forță majoră (eveniment imprevizibil, insurmontabil și exterior voinței PĂRȚILOR), cu obligația notificării celeilalte PĂRȚI în termen de 5 zile lucrătoare de la apariția evenimentului."),
      
      // ============ XI. SOLUȚIONAREA LITIGIILOR ============
      h2("XI. SOLUȚIONAREA LITIGIILOR"),
      
      p("Art. 24. Eventualele litigii izvorâte din executarea, interpretarea sau încetarea prezentului contract se soluționează pe cale amiabilă, prin negociere directă între PĂRȚI."),
      
      p("Art. 25. În cazul în care soluționarea amiabilă nu este posibilă, litigiile sunt de competența instanțelor judecătorești competente din Odorheiu Secuiesc, conform legislației române în vigoare."),
      
      // ============ XII. DISPOZIȚII FINALE ============
      h2("XII. DISPOZIȚII FINALE"),
      
      p("Art. 26. Modificarea prezentului contract se poate face numai prin acte adiționale scrise, semnate de ambele PĂRȚI."),
      
      p("Art. 27. Comunicările între PĂRȚI se fac în scris, prin email, fax sau scrisoare recomandată cu confirmare de primire, la următoarele adrese:"),
      pAlpha("·", "LOCATOR: Béla Iosif, str. Tamási Áron nr. 14, Odorheiu Secuiesc, email: bela.iosif@gmail.com, telefon: 0744-291.872;"),
      pAlpha("·", "LOCATAR: TransOffice Trade S.R.L., str. Calea Băieșenilor nr. 22, Odorheiu Secuiesc, email: contact@transoffice.ro, telefon: 0266-218.945."),
      
      p("Art. 28. Anexele 1 (Plan de amplasament) și 2 (Proces-verbal de predare-primire) fac parte integrantă din prezentul contract."),
      
      p("Art. 29. Prezentul contract a fost încheiat astăzi, 26 aprilie 2018, în 3 (trei) exemplare originale, în limba română, dintre care: un exemplar pentru LOCATOR, un exemplar pentru LOCATAR și un exemplar care va fi depus la organul fiscal pentru înregistrare."),
      
      p("Art. 30. Prezentul contract a fost citit, înțeles și aprobat de ambele PĂRȚI, fiind semnat de bună voie, fără vicii de consimțământ."),
      
      // ============ SIGNATURES ============
      new Paragraph({ children: [new TextRun("")], spacing: { before: 400 } }),
      
      new Paragraph({
        children: [
          new TextRun({ text: "LOCATOR,", bold: true, size: 22 }),
          new TextRun({ text: "\t\t\t\t\t" }),
          new TextRun({ text: "LOCATAR,", bold: true, size: 22 })
        ],
        tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
        spacing: { after: 80 }
      }),
      
      new Paragraph({
        children: [
          new TextRun({ text: "BÉLA IOSIF", bold: true, size: 22 }),
          new TextRun({ text: "\t\t\t\t\t" }),
          new TextRun({ text: "TRANSOFFICE TRADE S.R.L.", bold: true, size: 22 })
        ],
        tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
        spacing: { after: 40 }
      }),
      
      new Paragraph({
        children: [
          new TextRun({ text: "(persoană fizică)", size: 20, italics: true }),
          new TextRun({ text: "\t\t\t\t\t" }),
          new TextRun({ text: "prin administrator: KOVÁCS ISTVÁN", size: 20, italics: true })
        ],
        tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
        spacing: { after: 240 }
      }),
      
      new Paragraph({
        children: [
          new TextRun({ text: "_____________________", size: 22 }),
          new TextRun({ text: "\t\t\t\t\t" }),
          new TextRun({ text: "_____________________", size: 22 })
        ],
        tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
        spacing: { after: 200 }
      }),
      
      new Paragraph({
        children: [new TextRun({ text: "Contract înregistrat la ANAF Harghita sub nr. 8472 din 18.05.2018.", size: 18, italics: true, color: "555555" })],
        alignment: AlignmentType.LEFT,
        spacing: { before: 240 }
      })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/sessions/compassionate-focused-cerf/mnt/Haladó/Tananyag/01_Ceg_megertes/TransOffice/szerzodes_chirie_TransOffice_2018.docx", buffer);
  console.log("Bérleti szerződés generálva!");
  
  // PDF-et is generáljunk LibreOffice-szal
  const { execSync } = require('child_process');
  execSync('cd "/sessions/compassionate-focused-cerf/mnt/outputs/F4_legal_assets" && cp "/sessions/compassionate-focused-cerf/mnt/Haladó/Tananyag/01_Ceg_megertes/TransOffice/szerzodes_chirie_TransOffice_2018.docx" . && libreoffice --headless --convert-to pdf szerzodes_chirie_TransOffice_2018.docx 2>&1 | tail -3');
  console.log("PDF is generálva.");
});
