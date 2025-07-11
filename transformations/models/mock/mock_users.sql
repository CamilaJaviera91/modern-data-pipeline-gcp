{{ config(
    materialized='table',
    full_refresh=true
) }}

-- models/mock/mock_users.sql

WITH first_names AS (
    SELECT *
    FROM unnest(ARRAY[
            'Aarón', 'Abel', 'Abilio', 'Abraham', 'Adela', 'Adelia', 'Adelina', 'Adolfo', 'Adoración', 'Adrián',
            'Adán', 'Agapito', 'Ainara', 'Aitana', 'Aitor', 'Albina', 'Albino', 'Alejo', 'Alfonso', 'Alicia',
            'Amado', 'Amador', 'Amalia', 'Amanda', 'Amando', 'Amaro', 'Amaya', 'Amor', 'Amílcar', 'Ana',
            'Andrés Felipe', 'Angelina', 'Angelita', 'Ani', 'Anselma', 'Antonia', 'Antonio', 'Anunciación', 'Aníbal', 'Apolonia',
            'Araceli', 'Ariadna', 'Ariel', 'Armando', 'Aroa', 'Arsenio', 'Artemio', 'Asdrubal', 'Asunción', 'Aureliano',
            'Aurelio', 'Aurora', 'Azeneth', 'Baltasar', 'Basilio', 'Baudelio', 'Bautista', 'Belén', 'Benigna', 'Benigno',
            'Benjamín', 'Bernarda', 'Bernardo', 'Berta', 'Bibiana', 'Blas', 'Borja', 'Brunilda', 'Bruno', 'Brígida',
            'Buenaventura', 'Bárbara', 'Calista', 'Calisto', 'Calixta', 'Calixto', 'Camila', 'Candela', 'Candelaria', 'Candelario',
            'Caridad', 'Carlos', 'Carlota', 'Carmela', 'Carmelita', 'Carmen', 'Carmina', 'Carolina', 'Casandra', 'Cayetana',
            'Cayetano', 'Cebrián', 'Cecilia', 'Cecilio', 'Ceferino', 'Charo', 'Che', 'Chelo', 'Chucho', 'Chus',
            'Ciriaco', 'Cirino', 'Ciro', 'Ciríaco', 'Clara', 'Claudia', 'Cleto', 'Cloe', 'Clotilde', 'Clímaco',
            'Concepción', 'Cornelio', 'Corona', 'Cosme', 'Crescencia', 'Cristian', 'Cristina', 'Cristóbal', 'Cruz', 'Curro',
            'Custodia', 'Custodio', 'Cándido', 'César', 'Dafne', 'Dalila', 'Damián', 'Dani', 'Daniela', 'Darío',
            'David', 'Dimas', 'Dionisia', 'Dionisio', 'Dolores', 'Dominga', 'Dorotea', 'Dulce', 'Débora', 'Edelmiro',
            'Edgardo', 'Edu', 'Eduardo', 'Eladio', 'Elena', 'Eleuterio', 'Eligia', 'Eligio', 'Elisabet', 'Elodia',
            'Eloy', 'Eloísa', 'Elvira', 'Emelina', 'Emiliano', 'Emilio', 'Emma', 'Encarnación', 'Enrique', 'Eric',
            'Esperanza', 'Estefanía', 'Estela', 'Ester', 'Estrella', 'Eufemia', 'Eulalia', 'Eusebia', 'Eusebio', 'Eustaquio',
            'Evangelina', 'Ezequiel', 'Fabiana', 'Fabiola', 'Fabián', 'Fabricio', 'Fausto', 'Febe', 'Feliciana', 'Feliciano',
            'Felicidad', 'Felipa', 'Felix', 'Fermín', 'Fernanda', 'Fernando', 'Fidel', 'Filomena', 'Fito', 'Flavia',
            'Flavio', 'Flora', 'Florentina', 'Florinda', 'Francisca', 'Francisco Javier', 'Fátima', 'Félix', 'Gabriela', 'Galo',
            'Gaspar', 'Gastón', 'Gema', 'Genoveva', 'Georgina', 'Gervasio', 'Gilberto', 'Gisela', 'Goyo', 'Gracia',
            'Graciana', 'Gregorio', 'Griselda', 'Guadalupe', 'Haroldo', 'Haydée', 'Heliodoro', 'Heraclio', 'Herberto', 'Herminia',
            'Herminio', 'Hernando', 'Hilda', 'Hugo', 'Humberto', 'Héctor', 'Ibán', 'Ignacia', 'Ignacio', 'Iker',
            'Ildefonso', 'Imelda', 'Inmaculada', 'Inés', 'Iris', 'Irma', 'Isaac', 'Isabel', 'Isabela', 'Isaías',
            'Isidora', 'Isidoro', 'Isidro', 'Iván', 'Jacinta', 'Jacinto', 'Jafet', 'Javier', 'Javiera', 'Jenaro',
            'Jenny', 'Jeremías', 'Jessica', 'Joan', 'Joel', 'Jordi', 'Jordán', 'Jorge', 'Jose', 'Jose Angel',
            'Jose Carlos', 'Jose Ignacio', 'Jose Manuel', 'Jose Miguel', 'Jose Ramón', 'Josefina', 'Josep', 'José', 'José Manuel', 'Juan Carlos',
            'Juan Francisco', 'Juan José', 'Juan Luis', 'Juan Manuel', 'Juanito', 'Judith', 'Juliana', 'Julie', 'Julieta', 'Julio',
            'Julián', 'Lalo', 'Laura', 'Leandra', 'Leonardo', 'Leonel', 'Leopoldo', 'Leyre', 'León', 'Lilia',
            'Liliana', 'Lina', 'Loida', 'Lola', 'Lope', 'Lorena', 'Lorenza', 'Loreto', 'Lucas',
            'Lucho', 'Luciano', 'Luis Miguel', 'Luisa', 'Luisina', 'Luna', 'Lupe', 'Lupita', 'Lázaro', 'Macaria',
            'Magdalena', 'Maite', 'Manolo', 'Manu', 'Manuela', 'Manuelita', 'Marc', 'Marcela', 'Marcelino', 'Marcelo',
            'Marcial', 'Marciano', 'Marco', 'Marcos', 'Margarita', 'Mariana', 'Marianela', 'Maribel', 'Maricela', 'Maricruz',
            'Marino', 'Mario', 'Marisa', 'Marisol', 'Martin', 'Martina', 'Martirio', 'María Belén', 'María Carmen', 'María Dolores',
            'María Jesús', 'María José', 'María Manuela', 'María Teresa', 'Mateo', 'Maura', 'Mauricio', 'Maxi', 'Maximiano', 'Melania',
            'Melisa', 'Micaela', 'Miguela', 'Milagros', 'Mireia', 'Miriam', 'Mirta', 'Modesto', 'Moisés', 'Moreno',
            'Mónica', 'Nacho', 'Nadia', 'Nando', 'Natalia', 'Natalio', 'Natanael', 'Natividad', 'Nazaret', 'Nazario',
            'Nereida', 'Nicodemo', 'Nidia', 'Nilo', 'Noa', 'Noelia', 'Noemí', 'Norberto', 'Noé', 'Nuria',
            'Nydia', 'Obdulia', 'Olalla', 'Olegario', 'Olga', 'Omar', 'Onofre', 'Otilia', 'Paca', 'Paco',
            'Pancho', 'Pascual', 'Paula', 'Paulino', 'Paz', 'Pedro', 'Pepito', 'Perla', 'Perlita', 'Piedad',
            'Plinio', 'Porfirio', 'Primitivo', 'Prudencia', 'Prudencio', 'Pánfilo', 'Pía', 'Rafael', 'Raimundo', 'Raquel', 
            'Raúl', 'Rebeca', 'Regina', 'Reina', 'Renata', 'Reyes', 'Reyna', 'Reynaldo', 'Ricardo', 'Rico', 
            'Rita', 'Roberta', 'Roberto', 'Rogelio', 'Rosa María', 'Rosalina', 'Rosalinda', 'Rosalva', 'Rosario', 'Rosaura', 
            'Roxana', 'Ruth', 'Ruy', 'Sabas', 'Sabina', 'Salomé', 'Salomón', 'Salud', 'Salvador', 'Samuel', 
            'Sancho', 'Sandra', 'Santiago', 'Santos', 'Sara', 'Sarita', 'Saturnina', 'Sebastian', 'Segismundo', 'Selena', 'Serafina',
            'Sergio', 'Seve', 'Simón', 'Socorro', 'Sofía', 'Sol', 'Soledad', 'Sonia', 'Sosimo', 'Tania',
            'Tecla', 'Telmo', 'Teo', 'Teófilo', 'Tiburcio', 'Tito', 'Tomasa', 'Tomás', 'Toño', 'Trini',
            'Trinidad', 'Tristán', 'Urbano', 'Vanesa', 'Vasco', 'Venceslás', 'Vera', 'Vicenta', 'Vidal', 'Vilma',
            'Vito', 'Wilfredo', 'Wálter', 'Ximena', 'Xiomara', 'Yaiza', 'Zacarías', 'Zaida', 'Zaira', 'Zoraida',
            'Ágata', 'Águeda', 'Álvaro', 'Ámbar', 'Ángel', 'Ángela', 'Ángeles', 'Édgar', 'Óscar', 'Úrsula'
    ]) WITH ORDINALITY AS t(first_name, id)
),
last_names AS (
    SELECT *
    FROM unnest(ARRAY[
            'Abella', 'Acedo', 'Adán', 'Aguado', 'Aguiló', 'Agustí', 'Agustín', 'Alberola', 'Alcalá', 'Alcolea',
            'Alcántara', 'Alcázar', 'Alemany', 'Aliaga', 'Aller', 'Almagro', 'Almansa', 'Almazán', 'Almeida', 'Amat',
            'Amaya', 'Amigó', 'Amores', 'Andrade', 'Andres', 'Anguita', 'Antúnez', 'Aparicio', 'Aragonés', 'Araujo',
            'Arco', 'Arcos', 'Ariza', 'Ariño', 'Arjona', 'Armengol', 'Arranz', 'Arrieta', 'Arroyo', 'Arteaga',
            'Avilés', 'Ayllón', 'Ayuso', 'Aznar', 'Azorin', 'Baeza', 'Ballester', 'Barba', 'Barreda', 'Barrena',
            'Barrera', 'Barrios', 'Barroso', 'Baró', 'Bas', 'Bayona', 'Bayón', 'Baños', 'Belda', 'Bellido',
            'Beltran', 'Benavent', 'Benavides', 'Benet', 'Benitez', 'Berenguer', 'Bermúdez', 'Bernat', 'Berrocal', 'Bertrán',
            'Bilbao', 'Blanes', 'Blazquez', 'Blázquez', 'Boada', 'Bolaños', 'Borja', 'Bosch', 'Botella', 'Bou',
            'Bravo', 'Buendía', 'Bueno', 'Caballero', 'Cabanillas', 'Cabello', 'Cabeza', 'Cabezas', 'Cabo', 'Cabrera',
            'Cal', 'Calderon', 'Calvo', 'Camacho', 'Campillo', 'Campoy', 'Canet', 'Carballo', 'Carbonell', 'Carbó',
            'Cardona', 'Carmona', 'Carnero', 'Carpio', 'Carrasco', 'Carreras', 'Carrillo', 'Carrión', 'Carvajal', 'Casals',
            'Casanova', 'Casas', 'Cases', 'Castañeda', 'Castell', 'Castillo', 'Castro', 'Catalá', 'Catalán', 'Cañellas',
            'Cerdá', 'Cerezo', 'Cerro', 'Chacón', 'Chaves', 'Chico', 'Cisneros', 'Clemente', 'Cobos', 'Coca',
            'Coello', 'Colom', 'Coloma', 'Comas', 'Company', 'Contreras', 'Cordero', 'Cornejo', 'Corominas', 'Coronado',
            'Correa', 'Cortes', 'Crespi', 'Crespo', 'Cruz', 'Cuadrado', 'Cuenca', 'Cuevas', 'Céspedes', 'Córdoba',
            'Dalmau', 'Daza', 'Delgado', 'Diez', 'Doménech', 'Domínguez', 'Durán', 'Dávila', 'Díaz', 'Díez',
            'Echevarría', 'Echeverría', 'Escobar', 'Escolano', 'Escudero', 'Espada', 'Espinosa', 'Esteve', 'Expósito', 'Fabregat',
            'Falcó', 'Falcón', 'Farré', 'Feijoo', 'Feliu', 'Fernández', 'Ferrera', 'Ferreras', 'Figuerola', 'Fiol',
            'Flor', 'Flores', 'Font', 'Frutos', 'Fuertes', 'Gabaldón', 'Galan', 'Galiano', 'Galván', 'Galán',
            'Garay', 'Gargallo', 'Garzón', 'Gascón', 'Gaya', 'Gibert', 'Gilabert', 'Gimenez', 'Giménez', 'Giralt',
            'Gomez', 'Gomila', 'Gonzalez', 'Gordillo', 'Granados', 'Grau', 'Gual', 'Guardia', 'Guardiola', 'Guerra',
            'Guijarro', 'Guillen', 'Guitart', 'Gutierrez', 'Guzman', 'Gálvez', 'Gárate', 'Gómez', 'Haro', 'Heras',
            'Heredia', 'Hernandez', 'Hernando', 'Hernández', 'Herrero', 'Hervia', 'Hervás', 'Hidalgo', 'Hierro', 'Higueras',
            'Huertas', 'Hurtado', 'Ibañez', 'Ibáñez', 'Iglesia', 'Iglesias', 'Iniesta', 'Iriarte', 'Izquierdo', 'Jara',
            'Jaén', 'Jimenez', 'Jordán', 'Jove', 'Juan', 'Juárez', 'Lamas', 'Landa', 'Lara', 'Larrañaga',
            'Lasa', 'Lastra', 'Ledesma', 'Leon', 'León', 'Lillo', 'Llabrés', 'Lladó', 'Llamas', 'Llano',
            'Lledó', 'Llobet', 'Llorente', 'Lloret', 'Lluch', 'Lobo', 'Lorenzo', 'Losa', 'Luna', 'Luz',
            'Luís', 'Macias', 'Macías', 'Madrigal', 'Maestre', 'Maldonado', 'Malo', 'Manuel', 'Manzanares', 'Manzano',
            'Marcos', 'Mariscal', 'Marquez', 'Marqués', 'Marti', 'Martinez', 'Martín', 'Martínez', 'Marí', 'Mata',
            'Matas', 'Mate', 'Mateu', 'Mayo', 'Mayoral', 'Medina', 'Meléndez', 'Mendizábal', 'Menéndez', 'Mercader',
            'Merino', 'Mesa', 'Miranda', 'Moles', 'Moliner', 'Molins', 'Monreal', 'Montenegro', 'Montesinos', 'Montserrat',
            'Mora', 'Morales', 'Morante', 'Morata', 'Morcillo', 'Morillo', 'Morán', 'Mosquera', 'Moya', 'Murcia',
            'Muro', 'Mármol', 'Márquez', 'Mínguez', 'Múgica', 'Naranjo', 'Narváez', 'Navarrete', 'Nebot', 'Nevado',
            'Nieto', 'Niño', 'Nogueira', 'Núñez', 'Ochoa', 'Ojeda', 'Olivera', 'Oliveras', 'Olmo', 'Ortiz',
            'Ortuño', 'Pacheco', 'Palma', 'Palmer', 'Palomar', 'Paniagua', 'Pardo', 'Paredes', 'Pareja', 'Patiño',
            'Paz', 'Pedrero', 'Pedrosa', 'Peinado', 'Pellicer', 'Peláez', 'Pera', 'Perera', 'Perez', 'Pi',
            'Pinilla', 'Pinto', 'Pintor', 'Piquer', 'Pizarro', 'Piñeiro', 'Piñol', 'Pla', 'Plana', 'Planas',
            'Polo','Pont', 'Porcel', 'Porras', 'Porta', 'Prada', 'Prat', 'Priego', 'Puente', 'Puerta',
            'Puga', 'Puig', 'Pulido', 'Pérez', 'Quevedo', 'Quintero', 'Quiroga', 'Ramos', 'Ramón', 'Raya',
            'Real', 'Redondo', 'Reig', 'Requena', 'Reyes', 'Ribas', 'Ribera', 'Ribes', 'Ricart', 'Rico',
            'Rius', 'Rivera', 'Robles', 'Rodrigo', 'Rodríguez', 'Roig', 'Roldan', 'Romero', 'Romeu', 'Rosa',
            'Rosales', 'Rosselló', 'Roura', 'Rozas', 'Ruano', 'Río', 'Ríos', 'Saavedra', 'Sabater', 'Sacristán',
            'Saez', 'Sala', 'Salamanca', 'Salas', 'Salcedo', 'Sales', 'Salmerón', 'Salom', 'Samper', 'Sandoval',
            'Sanjuan', 'Sanmartín', 'Santiago', 'Sanz', 'Sarabia', 'Sastre', 'Saura', 'Segura', 'Serra', 'Serrano',
            'Sevilla', 'Simó', 'Sobrino', 'Sola', 'Solano', 'Solsona', 'Solís', 'Soria', 'Soriano', 'Sosa',
            'Soto', 'Sureda', 'Suárez', 'Sáenz', 'Taboada', 'Talavera', 'Tamayo', 'Tapia', 'Tejedor', 'Tejero',
            'Tirado', 'Tolosa', 'Tomas', 'Tomás', 'Tomé', 'Tormo', 'Torralba', 'Torrent', 'Torrents', 'Torres',
            'Tovar', 'Trillo', 'Tudela', 'Téllez', 'Ugarte', 'Uribe', 'Urrutia', 'Valbuena', 'Valdés', 'Valenciano',
            'Valentín', 'Vall', 'Valls', 'Vallés', 'Vargas', 'Velasco', 'Vera', 'Verdejo', 'Verdú', 'Vilar',
            'Villalba', 'Villanueva', 'Villaverde', 'Villegas', 'Villena', 'Vázquez', 'Vélez', 'Yáñez', 'Zamorano', 'Zorrilla'
    ]) WITH ORDINALITY AS t(last_name, id)
),
base AS (
    SELECT 
        generate_series(1, 1000) AS user_id,
        (random() * interval '365 days') AS random_date,
        floor(random() * 500 + 1)::int AS fn_id,
        floor(random() * 500 + 1)::int AS ln_id,
        CASE 
            WHEN random() > 0.5 THEN 'active'
            ELSE 'inactive'
        END AS status
),
user_data AS (
    SELECT
        b.user_id,
        fn.first_name,
        ln.last_name,
        CONCAT(fn.first_name, '_', ln.last_name, '_', b.user_id) AS username,
        CONCAT(fn.first_name, '.', ln.last_name, b.user_id, '@example.com') AS email,
        now() - b.random_date AS created_at,
        b.status,
        CASE
            WHEN b.status = 'active' THEN NULL
            ELSE b.random_date + now()
        END AS terminated_at
    FROM base b
    LEFT JOIN first_names fn ON b.fn_id = fn.id
    LEFT JOIN last_names ln ON b.ln_id = ln.id
)

SELECT * FROM user_data