import streamlit as st
import requests
import yfinance as yf
import pandas as pd

API_TOKEN = st.secrets["API_TOKEN"]

TICKERS = [
    "PETR4.SA","VALE3.SA","BBAS3.SA","MGLU3.SA","B3SA3.SA","COGN3.SA","ABEV3.SA","BBDC4.SA","ITSA4.SA","AZUL4.SA",
    "VAMO3.SA","ITUB4.SA","RAIZ4.SA","CSAN3.SA","CVCB3.SA","RAIL3.SA","PETR3.SA","PRIO3.SA","BEEF3.SA","CSNA3.SA",
    "MRFG3.SA","ASAI3.SA","MRVE3.SA","PETZ3.SA","BRFS3.SA","USIM5.SA","POMO4.SA","CPLE6.SA","LREN3.SA","RENT3.SA",
    "EMBR3.SA","VBBR3.SA","EQTL3.SA","RAPT4.SA","OIBR3.SA","CMIG4.SA","BRAV3.SA","GGBR4.SA","STBP3.SA","SUZB3.SA",
    "MOTV3.SA","MULT3.SA","MOVI3.SA","RADL3.SA","BRAP4.SA","SIMH3.SA","ECOR3.SA","ANIM3.SA","HAPV3.SA","WEGE3.SA",
    "UGPA3.SA","ELET3.SA","CMIN3.SA","BBDC3.SA","ENEV3.SA","IFCM3.SA","RDOR3.SA","BPAC11.SA","NTCO3.SA","GGPS3.SA",
    "SRNA3.SA","PCAR3.SA","CYRE3.SA","LWSA3.SA","CASH3.SA","CXSE3.SA","MLAS3.SA","VIVT3.SA","SMFT3.SA","TIMS3.SA",
    "GOAU4.SA","CBAV3.SA","KLBN11.SA","BBSE3.SA","ALOS3.SA","INTB3.SA","BRKM5.SA","HYPE3.SA","SBSP3.SA","ARML3.SA",
    "AMER3.SA","AZZA3.SA","AZTE3.SA","CPLE3.SA","BHIA3.SA","FLRY3.SA","ALPA4.SA","RECV3.SA","IGTI11.SA","IGTI11.SA",
    "SLCE3.SA","AURE3.SA","VIVA3.SA","JHSF3.SA","CEAB3.SA","GMAT3.SA","LJQQ3.SA","SMTO3.SA","HBSA3.SA","ENGI11.SA",
    "NEOE3.SA","CSMG3.SA","TOTS3.SA","SANB11.SA","RCSL4.SA","SAPR11.SA","SAPR4.SA","KLBN4.SA","YDUQ3.SA","QUAL3.SA",
    "SEQL3.SA","TTEN3.SA","ODPV3.SA","CAML3.SA","GRND3.SA","HBOR3.SA","DIRR3.SA","DXCO3.SA","LIGT3.SA","TAEE11.SA",
    "EGIE3.SA","ISAE4.SA","PSSA3.SA","SBFG3.SA","POSI3.SA","RANI3.SA","CPFE3.SA","PGMN3.SA","CURY3.SA","BRSR6.SA",
    "AZEV4.SA","MTRE3.SA","PDGR3.SA","AZEV3.SA","ELET6.SA","WIZC3.SA","EZTC3.SA","MILS3.SA","JSLG3.SA","PMAM3.SA",
    "IRBR3.SA","ALUP11.SA","TEND3.SA","VULC3.SA","PLPL3.SA","FRAS3.SA","ITUB3.SA","GFSA3.SA","BMGB4.SA","DASA3.SA",
    "GUAR3.SA","KEPL3.SA","BPAN4.SA","VVEO3.SA","HBRE3.SA","MDNE3.SA","LAND3.SA","ONCO3.SA","TFCO4.SA","MELK3.SA",
    "ZAMP3.SA","USIM3.SA","PTBL3.SA","MYPK3.SA","AMAR3.SA","SEER3.SA","AMOB3.SA","ORVR3.SA","JALL3.SA","BIOM3.SA",
    "TRIS3.SA","SAPR3.SA","SOJA3.SA","EVEN3.SA","MEAL3.SA","OPCT3.SA","BRST3.SA","TUPY3.SA","LAVV3.SA","FESA4.SA",
    "VLID3.SA","PORT3.SA","ENJU3.SA","MDIA3.SA","MATD3.SA","AERI3.SA","PINE4.SA","ABCB4.SA","BLAU3.SA","VTRU3.SA",
    "SYNE3.SA","TGMA3.SA","ESPA3.SA","CMIG3.SA","CSED3.SA","KLBN3.SA","RCSL3.SA","PNVL3.SA","PRNR3.SA","DESK3.SA",
    "SHUL4.SA","BRBI11.SA","LVTC3.SA","TASA4.SA","PFRM3.SA","LEVE3.SA","AMBP3.SA","RAPT3.SA","ITSA3.SA","LOGG3.SA",
    "VITT3.SA","POMO3.SA","FIQE3.SA","ROMI3.SA","UNIP6.SA","BMOB3.SA","AGXY3.SA","TAEE4.SA","LPSB3.SA","INEP3.SA",
    "SANB3.SA","ALPK3.SA","BRAP3.SA","INEP4.SA","AGRO3.SA","ETER3.SA","LUPA3.SA","GGBR3.SA","DMVF3.SA","SANB4.SA",
    "RNEW4.SA","OIBR4.SA","TECN3.SA","HOOT4.SA","DEXP3.SA","EUCA4.SA","TCSA3.SA","PDTC3.SA","VSTE3.SA","DOTZ3.SA",
    "RNEW3.SA","TAEE3.SA","UCAS3.SA","EALT4.SA","IGTI3.SA","IGTI3.SA","GOAU3.SA","RSID3.SA","TPIS3.SA","CGRA3.SA",
    "FICT3.SA","SHOW3.SA","VIVR3.SA","FHER3.SA","BOBR4.SA","HAGA4.SA","ALLD3.SA","BRKM3.SA","CSUD3.SA","CAMB3.SA",
    "AALR3.SA","BMEB4.SA","PTNT4.SA","BIED3.SA","TRAD3.SA","RPMG3.SA","ALUP4.SA","BAZA3.SA","NUTR3.SA","LOGN3.SA",
    "WHRL4.SA","EMAE4.SA","RNEW11.SA","JFEN3.SA","AVLL3.SA","SCAR3.SA","ALPA3.SA","ALUP3.SA","ATED3.SA","WHRL3.SA",
    "BRSR3.SA","BEES3.SA","AZEV11.SA","ENGI3.SA","AMAR11.SA","BPAC5.SA","MAPT4.SA","RDNI3.SA","CGRA4.SA","CEDO4.SA",
    "BGIP4.SA","CLSC4.SA","HAGA3.SA","BPAC3.SA","TASA3.SA","ISAE3.SA","CEBR6.SA","PINE3.SA","REAG3.SA","OFSA3.SA",
    "BALM4.SA","DEXP4.SA","UNIP3.SA","REDE3.SA","NGRD3.SA","BEES4.SA","TELB4.SA","EUCA3.SA","EPAR3.SA","WLMM4.SA",
    "TELB3.SA","BSLI4.SA","COCE5.SA","MNPR3.SA","DOHL4.SA","GSHP3.SA","MNDL3.SA","CEBR3.SA","ENGI4.SA","MTSA4.SA",
    "PPLA11.SA","BMEB3.SA","MGEL4.SA","CRPG5.SA","EQPA3.SA","WEST3.SA","CEEB3.SA","LUXM4.SA","PLAS3.SA","RPAD6.SA",
    "CEBR5.SA","OSXB3.SA","CGAS5.SA","BNBR3.SA","GEPA4.SA","RSUL4.SA","COCE3.SA","CRPG3.SA","BMIN4.SA","CPLE5.SA",
    "MWET4.SA","FIEI3.SA","NORD3.SA","CTSA4.SA","CGAS3.SA","MTSA3.SA","AHEB5.SA","AHEB3.SA","MRSA3B.SA","BALM3.SA",
    "BSLI3.SA","AFLT3.SA","RPAD3.SA","BMKS3.SA","MOAR3.SA","PATI3.SA","EKTR4.SA","BRSR5.SA","EALT3.SA","PINE11.SA",
    "NEXP3.SA","ELET5.SA","UNIP5.SA","PEAB3.SA","PATI4.SA","CCTY3.SA","CRPG6.SA","PTNT3.SA","CEED3.SA","RPAD5.SA",
    "ELMD3.SA","DTCY3.SA","SNSY5.SA","EQPA7.SA","SNSY3.SA","BGIP3.SA","BDLL4.SA","GOLL4.SA","JOPA3.SA","BDLL3.SA",
    "ENMT3.SA","CTKA4.SA","MWET3.SA","GEPA3.SA","EQMA3B.SA","TKNO4.SA","SOND5.SA","BMIN3.SA","CEEB5.SA","MRSA5B.SA",
    "MRSA6B.SA","ESTR4.SA","JBSS3.SA","JBSS3.SA","WLMM3.SA","EKTR3.SA","FESA3.SA","BRKM6.SA","ATMP3.SA","CLSC3.SA",
    "PEAB4.SA","BAUH4.SA","PSVM11.SA","CTSA3.SA","DOHL3.SA","SOND6.SA","CTKA3.SA","HBTS5.SA"
]

LANG_TEXT = {
    "title": {
        "en": "Magic Formula - B3 Ranked Analysis",
        "pt": "Fórmula Mágica - Análise Ranqueada B3"
    },
    "description": {
        "en": "Joel Greenblatt's Magic Formula is a systematic value investing strategy that helps investors find quality companies trading at attractive prices. It ranks stocks by Earnings Yield, which highlights undervalued opportunities, and Return on Capital, which measures how efficiently a company generates profits. Companies with higher Earnings Yield and higher Return on Capital are more likely to offer strong returns, as they combine attractive pricing with proven business performance.",
        "pt": "A Fórmula Mágica de Joel Greenblatt é uma estratégia sistemática de investimento em valor que ajuda investidores a encontrar empresas de qualidade negociadas a preços atrativos. Ela classifica ações pelo Earnings Yield, que destaca oportunidades subvalorizadas, e pelo Return on Capital, que mede a eficiência da geração de lucros. Empresas com altos índices nesses critérios tendem a oferecer retornos mais sólidos, pois unem preço atrativo e desempenho comprovado."
    },
    "formula": {
        "en": "**Magic Formula Score = (Earnings Yield) + (Return on Capital) * 0.33**",
        "pt": "**Pontuação Fórmula Mágica = (Earnings Yield) + (Return on Capital) * 0,33**"
    },
    "run_button": {
        "en": "Run Analysis",
        "pt": "Executar Análise"
    },
    "date_filter": {
        "en": "Filter by Report Date:",
        "pt": "Filtrar por Data do Balanço:"
    },
    "table_header": {
        "en": "Ranked Results (Positive EY and ROC)",
        "pt": "Resultados Rankeados (EY e ROC Positivos)"
    },
    "table_negative": {
        "en": "Tickers with Negative or Zero Earnings Yield or Return on Capital",
        "pt": "Ações com Earnings Yield ou Return on Capital Negativos ou Zero"
    },
    "ticker_counter": {
        "en": "Showing {n} stocks",
        "pt": "Exibindo {n} ações"
    },
    "no_data": {
        "en": "No data to display. Click 'Run Analysis' to begin.",
        "pt": "Nenhum dado para exibir. Clique em 'Executar Análise' para começar."
    },
    "fetch_summary": {
        "en": "Fetched {ok} tickers, {neg} with negative/zero, {fail} failed.",
        "pt": "Buscou {ok} ações, {neg} negativas/zero, {fail} falharam."
    }
}

if 'error_msgs' not in st.session_state:
    st.session_state.error_msgs = []
if 'dismissed_errors' not in st.session_state:
    st.session_state.dismissed_errors = set()

@st.cache_data(ttl=3600)
def get_usd_to_brl_rate():
    try:
        ticker = yf.Ticker("USDBRL=X")
        hist = ticker.history(period="1d")
        if not hist.empty: return hist['Close'].iloc[-1]
        st.error("Could not fetch USD/BRL exchange rate.")
        return None
    except Exception as e:
        st.error(f"yfinance error: {e}")
        return None

def get_financial_data(ticker):
    url = f"https://eodhd.com/api/fundamentals/{ticker}?api_token={API_TOKEN}&fmt=json"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        income_stmt_q = data.get('Financials', {}).get('Income_Statement', {}).get('quarterly', {})
        balance_sheet_q = data.get('Financials', {}).get('Balance_Sheet', {}).get('quarterly', {})
        if not income_stmt_q or not balance_sheet_q:
            return None, "No quarterly data"
        common_dates = sorted(set(income_stmt_q.keys()) & set(balance_sheet_q.keys()), reverse=True)
        for date in common_dates:
            income_report = income_stmt_q.get(date)
            balance_sheet_report = balance_sheet_q.get(date)
            if not income_report or not balance_sheet_report:
                continue
            ebit_usd = float(income_report.get('ebit') or 0)
            total_debt_brl = float(balance_sheet_report.get('shortLongTermDebtTotal') or 0)
            total_equity_brl = float(balance_sheet_report.get('totalStockholderEquity') or 0)
            enterprise_value_brl = float(data.get('Valuation', {}).get('EnterpriseValue', 0))
            if ebit_usd != 0 and (total_debt_brl != 0 or total_equity_brl != 0):
                return {
                    "report_date": date,
                    "ebit_usd": ebit_usd,
                    "enterprise_value_brl": enterprise_value_brl,
                    "total_debt_brl": total_debt_brl,
                    "total_equity_brl": total_equity_brl,
                }, None
        return None, "No valid report with nonzero EBIT and capital"
    except Exception as e:
        return None, f"Error: {str(e)}"

st.set_page_config(layout="wide")

# Sidebar: Language selection and error messages
with st.sidebar:
    lang = st.radio("Language / Idioma", options=["en", "pt"], format_func=lambda x: "English" if x == "en" else "Português")
    # Display closable error messages with subtle button
    if st.session_state.error_msgs:
        to_remove = []
        for i, msg in enumerate(st.session_state.error_msgs):
            if msg in st.session_state.dismissed_errors:
                continue
            cols = st.columns([0.93, 0.07])
            with cols[0]:
                st.warning(msg)
            with cols[1]:
                close_button = st.button("🗙", key=f"close_{i}", help="Dismiss", use_container_width=True)
                if close_button:
                    st.session_state.dismissed_errors.add(msg)
                    to_remove.append(msg)
        for msg in to_remove:
            st.session_state.error_msgs.remove(msg)

st.title(LANG_TEXT["title"][lang])
st.markdown(f"<p style='font-size:1.15em'>{LANG_TEXT['description'][lang]}</p>", unsafe_allow_html=True)
st.markdown(LANG_TEXT["formula"][lang])

if 'results_df' not in st.session_state:
    st.session_state.results_df = None
if 'all_dates' not in st.session_state:
    st.session_state.all_dates = []
if 'fetch_log' not in st.session_state:
    st.session_state.fetch_log = []

if st.button(LANG_TEXT["run_button"][lang]):
    st.session_state.error_msgs = []
    st.session_state.dismissed_errors = set()
    st.session_state.fetch_log = []
    rate = get_usd_to_brl_rate()
    if not rate:
        st.error("Cannot proceed without the BRL/USD exchange rate.")
    else:
        all_results = []
        all_dates = set()
        failed = []
        neg = []
        ok = []
        progress_bar = st.progress(0, text="Fetching data for tickers...")
        for i, ticker in enumerate(TICKERS):
            progress_text = f"Fetching data for {ticker} ({i+1}/{len(TICKERS)})"
            progress_bar.progress((i + 1) / len(TICKERS), text=progress_text)
            financials, err = get_financial_data(ticker)
            if financials:
                ebit_brl = financials["ebit_usd"] * rate
                ey_value = (ebit_brl / financials["enterprise_value_brl"]) * 100 if financials["enterprise_value_brl"] else 0
                capital_employed_brl = financials["total_debt_brl"] + financials["total_equity_brl"]
                capital_employed_usd = (capital_employed_brl / rate) if rate else 0
                roc_value = (financials["ebit_usd"] / capital_employed_usd) * 100 if capital_employed_usd else 0
                all_results.append({
                    "Ticker": ticker, "Report Date": financials["report_date"],
                    "Earnings Yield": ey_value, "Return on Capital": roc_value,
                })
                all_dates.add(financials["report_date"])
                if ey_value > 0 and roc_value > 0:
                    ok.append(ticker)
                else:
                    neg.append(ticker)
            else:
                failed.append(ticker)
                st.session_state.fetch_log.append(f"{ticker}: {err}")
        progress_bar.empty()
        if all_results:
            df = pd.DataFrame(all_results)
            df['Weighted Score'] = (df['Earnings Yield'] * 1) + (df['Return on Capital'] * 0.33)
            # Only rank positive tickers
            df['Magic Rank'] = None
            mask_positive = (df["Earnings Yield"] > 0) & (df["Return on Capital"] > 0)
            df.loc[mask_positive, 'Magic Rank'] = df.loc[mask_positive, 'Weighted Score'].rank(method='min', ascending=False).astype(int)
            st.session_state.results_df = df
            st.session_state.all_dates = sorted(list(all_dates), reverse=True)
            st.session_state.fetch_summary = LANG_TEXT["fetch_summary"][lang].format(
                ok=len(ok), neg=len(neg), fail=len(failed)
            )
        else:
            st.session_state.results_df = None
            st.session_state.all_dates = []
            st.session_state.fetch_summary = LANG_TEXT["fetch_summary"][lang].format(ok=0, neg=0, fail=len(TICKERS))

# --- Display Logic ---
if st.session_state.results_df is not None and not st.session_state.results_df.empty:
    df = st.session_state.results_df.copy()
    # Date filter
    if st.session_state.all_dates:
        selected_dates = st.multiselect(
            LANG_TEXT["date_filter"][lang],
            options=st.session_state.all_dates,
            default=st.session_state.all_dates
        )
        if selected_dates:
            df = df[df["Report Date"].isin(selected_dates)]

    # Split positive and negative
    df_positive = df[(df["Earnings Yield"] > 0) & (df["Return on Capital"] > 0)].copy()
    df_positive = df_positive.sort_values(by='Magic Rank')
    df_negative = df[~((df["Earnings Yield"] > 0) & (df["Return on Capital"] > 0))].copy()
    df_negative = df_negative.sort_values(by='Weighted Score', ascending=False)

    st.markdown("---")
    st.info(st.session_state.fetch_summary)
    if st.session_state.fetch_log:
        with st.expander("Show failed tickers and reasons"):
            for log in st.session_state.fetch_log:
                st.write(log)

    st.subheader(LANG_TEXT["table_header"][lang])
    st.markdown(
        f"**{LANG_TEXT['ticker_counter'][lang].format(n=len(df_positive))}**"
    )
    st.dataframe(
        df_positive[["Ticker", "Report Date", "Earnings Yield", "Return on Capital", "Weighted Score", "Magic Rank"]],
        column_config={
            "Earnings Yield": st.column_config.NumberColumn(format="%.2f%%"),
            "Return on Capital": st.column_config.NumberColumn(format="%.2f%%"),
            "Weighted Score": st.column_config.NumberColumn(format="%.2f"),
            "Magic Rank": st.column_config.NumberColumn()
        },
        use_container_width=True,
        hide_index=True,
    )

    if not df_negative.empty:
        st.markdown("---")
        st.subheader(LANG_TEXT["table_negative"][lang])
        st.markdown(
            f"**{LANG_TEXT['ticker_counter'][lang].format(n=len(df_negative))}**"
        )
        st.dataframe(
            df_negative[["Ticker", "Report Date", "Earnings Yield", "Return on Capital", "Weighted Score"]],
            column_config={
                "Earnings Yield": st.column_config.NumberColumn(format="%.2f%%"),
                "Return on Capital": st.column_config.NumberColumn(format="%.2f%%"),
                "Weighted Score": st.column_config.NumberColumn(format="%.2f")
            },
            use_container_width=True,
            hide_index=True,
        )
else:
    st.info(LANG_TEXT["no_data"][lang])
