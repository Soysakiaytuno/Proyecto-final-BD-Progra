USE [master]
GO
/****** Object:  Database [Proyecto Zoologico]    Script Date: 14/12/2024 07:50:05 p. m. ******/
CREATE DATABASE [Proyecto Zoologico]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Proyecto Zoologico', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Proyecto Zoologico.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Proyecto Zoologico_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Proyecto Zoologico_log.ldf' , SIZE = 73728KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [Proyecto Zoologico] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Proyecto Zoologico].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Proyecto Zoologico] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET ARITHABORT OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Proyecto Zoologico] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Proyecto Zoologico] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Proyecto Zoologico] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Proyecto Zoologico] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET RECOVERY FULL 
GO
ALTER DATABASE [Proyecto Zoologico] SET  MULTI_USER 
GO
ALTER DATABASE [Proyecto Zoologico] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Proyecto Zoologico] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Proyecto Zoologico] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Proyecto Zoologico] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Proyecto Zoologico] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Proyecto Zoologico] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'Proyecto Zoologico', N'ON'
GO
ALTER DATABASE [Proyecto Zoologico] SET QUERY_STORE = ON
GO
ALTER DATABASE [Proyecto Zoologico] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [Proyecto Zoologico]
GO
/****** Object:  Table [dbo].[Animales]    Script Date: 14/12/2024 07:50:05 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Animales](
	[ID.Animales] [int] NOT NULL,
	[Nombre] [nchar](10) NULL,
	[Especie] [nchar](10) NULL,
	[ModifiedDate] [date] NULL,
 CONSTRAINT [PK_Animales] PRIMARY KEY CLUSTERED 
(
	[ID.Animales] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Boleto]    Script Date: 14/12/2024 07:50:05 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Boleto](
	[ID.Zona] [int] NULL,
	[ID.Factura] [int] NULL,
	[Precio] [nchar](10) NULL,
	[ModifiedDate] [date] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cliente]    Script Date: 14/12/2024 07:50:05 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cliente](
	[ID.Cliente] [int] NOT NULL,
	[Nombre] [nchar](10) NULL,
	[Apellido] [nchar](10) NULL,
	[ModifiedDate] [date] NULL,
 CONSTRAINT [PK_Cliente] PRIMARY KEY CLUSTERED 
(
	[ID.Cliente] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Empleado]    Script Date: 14/12/2024 07:50:05 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Empleado](
	[ID.Empleado] [int] NOT NULL,
	[ID.Zona] [int] NOT NULL,
	[Nombre] [nchar](10) NULL,
	[Apellido] [nchar](10) NULL,
	[Area de trabajo] [nvarchar](50) NULL,
	[ModifiedDate] [date] NULL,
 CONSTRAINT [PK_Empleado] PRIMARY KEY CLUSTERED 
(
	[ID.Empleado] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Factura]    Script Date: 14/12/2024 07:50:05 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Factura](
	[ID.Cliente] [int] NULL,
	[ID.Factura] [int] NOT NULL,
	[ModifiedDate] [date] NULL,
 CONSTRAINT [PK_Factura] PRIMARY KEY CLUSTERED 
(
	[ID.Factura] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Zonas]    Script Date: 14/12/2024 07:50:05 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Zonas](
	[ID.Zona] [int] NOT NULL,
	[ID.Animal] [int] NULL,
	[Tipo de fauna] [nvarchar](50) NULL,
	[ModifiedDate] [date] NULL,
 CONSTRAINT [PK_Zonas] PRIMARY KEY CLUSTERED 
(
	[ID.Zona] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (1, N'Capibara  ', N'Roedor    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (2, N'Tigre     ', N'Felino    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (3, N'Mono      ', N'Primate   ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (4, N'Delfin    ', N'Bufeos    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (5, N'Loro      ', N'Ave       ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (6, N'Jaguar    ', N'Felino    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (7, N'Mono Leon ', N'Primate   ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (8, N'Vibora    ', N'Reptiles  ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (9, N'Pez dorado', N'Ciprínidos', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Animales] ([ID.Animales], [Nombre], [Especie], [ModifiedDate]) VALUES (10, N'Condor    ', N'Ave       ', CAST(N'2024-12-14' AS Date))
GO
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (110, 40, N'20        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (120, 41, N'30        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (130, 42, N'10        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (140, 43, N'15        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (150, 44, N'25        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (160, 45, N'15        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (170, 46, N'10        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (180, 47, N'25        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (190, 48, N'35        ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Boleto] ([ID.Zona], [ID.Factura], [Precio], [ModifiedDate]) VALUES (1010, 49, N'15        ', CAST(N'2024-12-14' AS Date))
GO
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (70, N'Diego     ', N'Martinez  ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (71, N'Laura     ', N'Garcia    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (72, N'Jose      ', N'Ruiz      ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (73, N'Ana       ', N'Torrez    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (74, N'Luis      ', N'Fernandez ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (75, N'Marta     ', N'Medrano   ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (76, N'Carlos    ', N'Sanchez   ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (77, N'Maria     ', N'Ramirez   ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (78, N'Dariana   ', N'Pol       ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (79, N'Elena     ', N'Martinez  ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Cliente] ([ID.Cliente], [Nombre], [Apellido], [ModifiedDate]) VALUES (770, N'Bruno     ', N'Diaz      ', CAST(N'2024-12-14' AS Date))
GO
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (21, 110, N'Juan      ', N'Perez     ', N'Limpieza  ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (22, 110, N'Maria     ', N'Gonzales  ', N'Seguridad ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (23, 110, N'Carlos    ', N'Ramirez   ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (24, 120, N'Ana       ', N'Fernandez ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (25, 120, N'Luis      ', N'Martinez  ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (26, 120, N'Carmen    ', N'Rodriguez ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (27, 130, N'Jose      ', N'Lopez     ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (28, 130, N'Elena     ', N'Garcia    ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (29, 130, N'Miguel    ', N'Sanchez   ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (220, 140, N'Laura     ', N'Torrez    ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (221, 140, N'Francisco ', N'Ruiz      ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (222, 140, N'Marta     ', N'Hernandez ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (223, 150, N'Pedro     ', N'Gomez     ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (224, 150, N'Isabel    ', N'Morales   ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (225, 150, N'Roberto   ', N'Ortiz     ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (226, 160, N'Claudia   ', N'Mendez    ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (227, 160, N'Ricardo   ', N'Diaz      ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (228, 160, N'Silvia    ', N'Castro    ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (229, 170, N'Zelda     ', N'Flores    ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2220, 170, N'Javier    ', N'Delgado   ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2221, 170, N'Andrea    ', N'Vargas    ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2222, 180, N'Fernando  ', N'Navarro   ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2223, 180, N'Patricia  ', N'Romero    ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2224, 180, N'Gabriel   ', N'Campos    ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2225, 190, N'Rosa      ', N'Suarez    ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2226, 190, N'Diego     ', N'Nuñez     ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2227, 190, N'Teresa    ', N'Medina    ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2228, 1010, N'Daniel    ', N'Rios      ', N'Limpieza', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (2229, 1010, N'Enrique   ', N'Paredes   ', N'Seguridad', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Empleado] ([ID.Empleado], [ID.Zona], [Nombre], [Apellido], [Area de trabajo], [ModifiedDate]) VALUES (22220, 1010, N'Natalia   ', N'Guerrero  ', N'Veterinaria', CAST(N'2024-12-14' AS Date))
GO
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (70, 40, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (71, 41, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (72, 42, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (73, 43, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (74, 44, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (75, 45, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (76, 46, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (77, 47, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (78, 48, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (79, 49, CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Factura] ([ID.Cliente], [ID.Factura], [ModifiedDate]) VALUES (770, 440, CAST(N'2024-12-14' AS Date))
GO
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (110, 9, N'Acuario   ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (120, 2, N'Selva     ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (130, 3, N'Bosque    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (140, 7, N'Bosque    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (150, 8, N'Bosque    ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (160, 1, N'Bosque Tropical', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (170, 6, N'Selva     ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (180, 5, N'Selva     ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (190, 4, N'Acuario   ', CAST(N'2024-12-14' AS Date))
INSERT [dbo].[Zonas] ([ID.Zona], [ID.Animal], [Tipo de fauna], [ModifiedDate]) VALUES (1010, 10, N'Montaña   ', CAST(N'2024-12-14' AS Date))
GO
ALTER TABLE [dbo].[Boleto]  WITH CHECK ADD  CONSTRAINT [FK_Boleto_Factura] FOREIGN KEY([ID.Factura])
REFERENCES [dbo].[Factura] ([ID.Factura])
GO
ALTER TABLE [dbo].[Boleto] CHECK CONSTRAINT [FK_Boleto_Factura]
GO
ALTER TABLE [dbo].[Boleto]  WITH CHECK ADD  CONSTRAINT [FK_Boleto_Zonas] FOREIGN KEY([ID.Zona])
REFERENCES [dbo].[Zonas] ([ID.Zona])
GO
ALTER TABLE [dbo].[Boleto] CHECK CONSTRAINT [FK_Boleto_Zonas]
GO
ALTER TABLE [dbo].[Empleado]  WITH CHECK ADD  CONSTRAINT [FK_Empleado_Zonas] FOREIGN KEY([ID.Zona])
REFERENCES [dbo].[Zonas] ([ID.Zona])
GO
ALTER TABLE [dbo].[Empleado] CHECK CONSTRAINT [FK_Empleado_Zonas]
GO
ALTER TABLE [dbo].[Factura]  WITH CHECK ADD  CONSTRAINT [FK_Factura_Cliente] FOREIGN KEY([ID.Cliente])
REFERENCES [dbo].[Cliente] ([ID.Cliente])
GO
ALTER TABLE [dbo].[Factura] CHECK CONSTRAINT [FK_Factura_Cliente]
GO
ALTER TABLE [dbo].[Zonas]  WITH CHECK ADD  CONSTRAINT [FK_Zonas_Animales] FOREIGN KEY([ID.Animal])
REFERENCES [dbo].[Animales] ([ID.Animales])
GO
ALTER TABLE [dbo].[Zonas] CHECK CONSTRAINT [FK_Zonas_Animales]
GO
USE [master]
GO
ALTER DATABASE [Proyecto Zoologico] SET  READ_WRITE 
GO
