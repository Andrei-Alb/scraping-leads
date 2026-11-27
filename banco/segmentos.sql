-- Segmentação dos leads por presença online. View, não tabela: recalcula sozinha quando entram empresas novas.
DROP VIEW IF EXISTS segmentos;
CREATE VIEW segmentos AS
SELECT
  e.place_id,
  e.nome,
  e.categoria,
  e.telefone,
  e.site,
  e.nota,
  e.avaliacoes,
  en.bairro,
  en.cidade,
  CASE
    WHEN e.site IS NULL THEN 'sem_nada'
    WHEN e.site LIKE '%instagram.com%' OR e.site LIKE '%facebook.com%' OR e.site LIKE '%wa.me%'
      OR e.site LIKE '%whatsapp%' OR e.site LIKE '%linktr.ee%' THEN 'so_rede_social'
    ELSE 'site_proprio'
  END AS presenca,
  -- Avaliações indicam movimento; nota alta indica negócio saudável que pode pagar.
  CASE
    WHEN e.avaliacoes >= 20 AND e.nota >= 4.3 THEN 'quente'
    WHEN e.avaliacoes >= 20 THEN 'morno'
    ELSE 'frio'
  END AS prioridade
FROM empresas e
JOIN enderecos en USING (place_id)
WHERE en.cidade IN ('Santarém', '') OR en.cidade IS NULL;
