-- Script para criar a View dos municípios no PostgreSQL
CREATE OR REPLACE VIEW public.vw_municipios_relevantes AS
SELECT 
    "SG_UF_ESC" as estado, 
    "NO_MUNICIPIO_ESC" as municipio, -- Ajustado para bater com o Power BI
    AVG("NU_NOTA_MT") as media_matematica,
    AVG("NU_NOTA_CH") as media_humanas,
    AVG("NU_NOTA_CN") as media_natureza,
    AVG("NU_NOTA_LC") as media_linguagens,
    AVG("NU_NOTA_REDACAO") as media_redacao,
    COUNT(*) as total_alunos
FROM public.enem_resultados_limpos
GROUP BY "SG_UF_ESC", "NO_MUNICIPIO_ESC";