let outerIDs = [-1, -1];
let outerContainerID = 1;

// Getter para outerIDs
function getOuterIDs() {
    console.log("Obtuviste outerIDs ", outerIDs)
    return outerIDs;
}

// Setter para outerIDs
function setOuterIDs(newIDs) {
    outerIDs = newIDs;
    console.log("Estableciste outerIDs ", outerIDs)
}

// Getter y Setter para outerContainerID
function getOuterContainerID() {
    console.log("Leiste newContainerID ", outerContainerID)
    return outerContainerID;
}

function setOuterContainerID(newContainerID) {
    outerContainerID = newContainerID;
    console.log("Estableciste newContainerID ", outerContainerID)
}

export { getOuterIDs, setOuterIDs, getOuterContainerID, setOuterContainerID };