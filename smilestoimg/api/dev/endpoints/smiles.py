import functools
import urllib.parse

from fastapi import APIRouter
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from starlette.responses import Response

router = APIRouter()


@functools.lru_cache(100000)
def smiles_to_image(smiles: str):

    smiles_parser = Chem.rdmolfiles.SmilesParserParams()
    smiles_parser.removeHs = False

    rdkit_molecule = Chem.MolFromSmiles(smiles, smiles_parser)

    if not rdkit_molecule.GetNumConformers():
        Chem.rdDepictor.Compute2DCoords(rdkit_molecule)

    drawer = rdMolDraw2D.MolDraw2DSVG(200, 200, 150, 200)
    drawer.drawOptions().padding = 0.05

    drawer.SetOffset(25, 0)
    drawer.DrawMolecule(rdkit_molecule)

    drawer.FinishDrawing()

    svg_content = drawer.GetDrawingText()
    svg_response = Response(svg_content, media_type="image/svg+xml")

    return svg_response


@router.get("/{smiles}")
async def get_molecule_image(smiles: str):
    return smiles_to_image(urllib.parse.unquote(smiles))
