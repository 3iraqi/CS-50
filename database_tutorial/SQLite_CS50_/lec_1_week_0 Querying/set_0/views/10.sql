SELECT english_title AS 'Hokusai`s prints ordered by brightness'
FROM views
WHERE artist ='Hokusai'
ORDER BY brightness DESC
;