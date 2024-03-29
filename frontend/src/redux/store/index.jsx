import { createStore, applyMiddleware } from "redux";
import rootReducer from "../reducer";
import createSagaMiddleware from "redux-saga";
import mySaga from "../saga";

const sagaMiddleware = createSagaMiddleware();

export default createStore(rootReducer, applyMiddleware(sagaMiddleware));

sagaMiddleware.run(mySaga);
