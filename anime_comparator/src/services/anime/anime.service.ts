import http from "@/services/shared/http-common"
async function getFullAnimeImages() {
    try{
        const response = await http.get("/getAnimeImageList")
        return response.data;
    } catch (error) {
        console.log("Ocurrio un error al cargar todas las imagenes de los animes:  ", error)
        return []
    }
}

async function getFullAnimeNames() {
    try{
        const response = await http.get("/getAnimeList")
        return response.data;
    } catch (error) {
        console.log("Ocurrio un error al cargar toda la información de los animes:  ", error)
        return []
    }
}

async function getAnimeGenresList() {
    try{
        const response = await http.get("/getAnimeGenres")
        return response.data;
    } catch (error) {
        console.log("Ocurrio un error al cargar los generos de los animes disponibles:  ", error)
        return []
    }
}

async function getAnimeFullDataList() {
    try{
        const response = await http.get("/getFullAnimeData")
        return response.data;
    } catch (error) {
        console.log("Ocurrio un error al cargar los generos de los animes disponibles:  ", error)
        return []
    }
}


async function getAnimeImageByID(id: number){
    try{
        const response = await http.get(`/getAnimeImage?id${id}`)
        return response.data;
    } catch (error) {
        console.log("Ocurrio un error al cargar la imagen de un anime: ", error)
        return "images/noimage.png"
    }
}

async function getAnimeInfoByID(id: number){
    try{
        const response = await http.get(`/getAnimeData?id=${id}`)
        return response.data;
    } catch (error) {
        console.log("Ocurrio un error al cargar la informacion completa de un anime: ", error)
        return {
            titleEnglish: "UNKNOWN",
            titleRomaji: "UNKNOWN",
            startDate: "??/??/????",
            endDate: "??/??/????",
            format: "UNKNOWN",
            genres: [],
            popularity: -1,
            score: -1,
            image: "images/noimage.png"
        }
    }
}

async function compareTwoAnimes(ID1: number, ID2: number){
    const response = await http.get(`/compare?id1=${ID1}&id2=${ID2}`)
    return response.data.result;
}



export {compareTwoAnimes, getAnimeImageByID, getFullAnimeNames, getAnimeInfoByID, getFullAnimeImages, getAnimeGenresList, getAnimeFullDataList}