let dataTable;
let dataTableIsInitialized = false;

const searchByName = (query, cryptos) => {
    return cryptos.filter((crypto) =>
        crypto.name.toLowerCase().includes(query.toLowerCase())
    );
};

const filterByPrice = (condition, cryptos) => {
    return cryptos.filter((crypto) => {
        if (condition === 'less') {
            return crypto.price < 10000; // Cambia el valor según tu criterio
        } else if (condition === 'greater') {
            return crypto.price >= 10000; // Cambia el valor según tu criterio
        }
        return true; // Si no hay filtro, devolver todas las criptomonedas
    });
};
const getBinancePrices = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/app/get_binance_prices/");
        const data = await response.json();
        
        // Verifica si la respuesta contiene la información esperada
        if (!data || !data.prices) {
            console.warn('Respuesta inesperada de Binance para obtener precios:', data);
            throw new Error('Respuesta inesperada de Binance para obtener precios');
        }

        return data.prices;
    } catch (ex) {
        console.error('Error al obtener los precios de Binance:', ex);
        throw new Error('Error al obtener los precios de Binance');
    }
};

const getBinanceCryptoInfo = async (symbol) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/app/get_binance_crypto_info/${symbol}/`);
        const data = await response.json();

        // Asegúrate de que la respuesta contenga la información esperada
        if (!data || !data.info || !data.info.price) {
            console.warn(`Respuesta inesperada de Binance para la criptomoneda ${symbol}:`, data);
            throw new Error('Respuesta inesperada de Binance para la criptomoneda');
        }

        return data.info;
    } catch (ex) {
        console.error(`Error al obtener la información de Binance para la criptomoneda ${symbol}:`, ex);
        throw new Error('Error al obtener la información de Binance para la criptomoneda');
    }
};

const listCryptos = async () => {
    try {
        const binancePrices = await getBinancePrices();

        const response = await fetch("http://127.0.0.1:8000/app/list_cryptos/");
        const data = await response.json();
        console.log('Data from listCryptos:', data);

        // Verifica si hay datos disponibles
        if (!data.cryptos || data.cryptos.length === 0) {
            console.warn('No hay criptomonedas disponibles en la respuesta de la API.');
            // Puedes mostrar un mensaje en la interfaz de usuario o realizar otras acciones apropiadas.
            return;
        }

        // Obtener valores de búsqueda y filtro
        const searchQuery = document.getElementById('search').value;
        const priceFilter = document.getElementById('priceFilter').value;

        let filteredCryptos = data.cryptos;

        // Aplicar búsqueda
        if (searchQuery) {
            filteredCryptos = searchByName(searchQuery, filteredCryptos);
        }

        // Aplicar filtro de precio
        if (priceFilter) {
            filteredCryptos = filterByPrice(priceFilter, filteredCryptos);
        }

        let content = '';
        for (let index = 0; index < filteredCryptos.length; index++) {
            const crypto = filteredCryptos[index];

            // Asegúrate de que crypto.symbol esté definido
            if (!crypto.symbol) {
                console.warn(`La criptomoneda en el índice ${index} no tiene un símbolo definido.`);
                continue;  // Salta a la siguiente iteración si no hay símbolo
            }

            const binanceInfo = await getBinanceCryptoInfo(crypto.symbol);

            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${crypto.name}</td>
                    <td>$${binanceInfo.price}</td>
                </tr>`;
        }

        document.getElementById("tableBody_cryptos").innerHTML = content;

        // Destruye y vuelve a inicializar la tabla DataTable
        if (dataTableIsInitialized) {
            dataTable.destroy();
        }

        dataTable = $("#datatable-cryptos").DataTable({
            columns: [
                { data: "#" },
                { data: "Name" },
                { data: "Price" }
            ],
            columnDefs: [
                { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
                { orderable: false, targets: [5, 6] },
                { searchable: false, targets: [0, 5, 6] }
            ],
            pageLength: 4,
            destroy: true
        });

        dataTableIsInitialized = true;
    } catch (ex) {
        console.error('Error al listar criptomonedas:', ex);
        // O muestra el mensaje de error en la interfaz de usuario
        // (por ejemplo, usando un elemento <div> en lugar de alert)
        //alert('Se produjo un error al listar criptomonedas. Consulta la consola para más detalles.');
    }
};

window.addEventListener("load", async () => {
    await listCryptos();
});

// Evento de cambio en el campo de búsqueda
$('#search').on('input', async function () {
    await listCryptos();
});

// Evento de cambio en el filtro de precio
$('#priceFilter').change(async function () {
    await listCryptos();
});