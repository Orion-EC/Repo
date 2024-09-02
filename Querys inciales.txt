-- Bd

CREATE DATABASE MundoFarma
    DEFAULT CHARACTER SET = 'utf8mb4';

-- Tablas

CREATE TABLE producto(  
    ID_Producto INT AUTO_INCREMENT PRIMARY KEY,
    Nombre_Producto varchar(255) NOT NULL,
    Componente_Producto varchar(255),
    INDEX (Nombre_Producto)
);

CREATE TABLE DetalleProducto (
    ID_Detalle INT AUTO_INCREMENT PRIMARY KEY,
    Precio FLOAT(9,2) NOT NULL,
    Fecha DATE,
    Farmacia VARCHAR(255),
    Link TEXT,
    ID_Producto INT,
  FOREIGN KEY (ID_Producto) REFERENCES Producto(ID_Producto)
);

-- Datos iniciales (1/2)

INSERT INTO 
  producto (
    `Nombre_Producto`, 
    `Componente_Producto`
  )
VALUES
  (
    "Nastizol", 
    "nasti+zol"
  );
  
-- Verificar datos

SELECT `ID_Producto`,`Nombre_Producto`,`Componente_Producto` FROM producto;


-- Datos iniciales (2/2)


INSERT INTO 
    detalleproducto (
      `Precio`, 
      `Fecha`, 
      `Farmacia`, 
      `Link`, 
      `ID_Producto`
    )
 VALUES
    (
      2500, 
      "2024-09-02", 
      "Farmacia Ahumada", 
      "si", 
      1
    );
    
-- Verificar datos

SELECT `ID_Detalle`,`Precio`,`Fecha`,`Farmacia`,`Link`,`ID_Producto` FROM detalleproducto;