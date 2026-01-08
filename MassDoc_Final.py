{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMl+AWA6WZJx6XAELhyTjqj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Mavivfernanda2/Masterdocument/blob/main/MassDoc_Final.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sYEtQrwpg4HO",
        "outputId": "76671c02-687b-4f8f-dfdf-745f95e4bcd8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.52.2)\n",
            "Requirement already satisfied: pymupdf in /usr/local/lib/python3.12/dist-packages (1.26.7)\n",
            "Requirement already satisfied: pillow in /usr/local/lib/python3.12/dist-packages (11.3.0)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.4)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.3.1)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.5.1)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.25.1)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.13.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.3)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2025.11.12)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (25.4.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.30.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit pymupdf pillow\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "os.makedirs(\"utils\", exist_ok=True)\n",
        "os.makedirs(\"output\", exist_ok=True)\n"
      ],
      "metadata": {
        "id": "B4Lj6W6sg_-A"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile utils/converter.py\n",
        "import fitz\n",
        "import os\n",
        "\n",
        "def pdf_to_png(pdf_path, output_dir, dpi=300):\n",
        "    doc = fitz.open(pdf_path)\n",
        "    images = []\n",
        "\n",
        "    zoom = dpi / 72\n",
        "    mat = fitz.Matrix(zoom, zoom)\n",
        "\n",
        "    for i, page in enumerate(doc):\n",
        "        pix = page.get_pixmap(matrix=mat)\n",
        "        out = os.path.join(output_dir, f\"page_{i+1}.png\")\n",
        "        pix.save(out)\n",
        "        images.append(out)\n",
        "\n",
        "    return images\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zHI70JXVhCSA",
        "outputId": "9497b64b-13ad-4311-97bf-0b6ee793cfa5"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing utils/converter.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile utils/school.py\n",
        "def school_preset(doc_type):\n",
        "    presets = {\n",
        "        \"Rapor\": {\"dpi\":300, \"wm\":True, \"prefix\":\"RAPOR\"},\n",
        "        \"Soal Ujian\": {\"dpi\":200, \"wm\":False, \"prefix\":\"SOAL\"},\n",
        "        \"Nilai\": {\"dpi\":300, \"wm\":True, \"prefix\":\"NILAI\"},\n",
        "        \"Surat Resmi\": {\"dpi\":300, \"wm\":True, \"prefix\":\"SURAT\"}\n",
        "    }\n",
        "    return presets[doc_type]\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xi4AKHclhFa9",
        "outputId": "37206823-35c7-417c-9bc9-bba8e05a7a81"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing utils/school.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile utils/watermark.py\n",
        "from PIL import Image, ImageDraw\n",
        "\n",
        "def add_watermark(img_path, text):\n",
        "    img = Image.open(img_path).convert(\"RGBA\")\n",
        "    draw = ImageDraw.Draw(img)\n",
        "\n",
        "    draw.text(\n",
        "        (20, img.height - 40),\n",
        "        text,\n",
        "        fill=(150,150,150,120)\n",
        "    )\n",
        "\n",
        "    img.save(img_path)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j8aqhlrkhIjY",
        "outputId": "40d75a1b-f901-4694-b0fd-ad57630a8986"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing utils/watermark.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile utils/zipper.py\n",
        "import zipfile\n",
        "import os\n",
        "\n",
        "def make_zip(folder, zip_path):\n",
        "    with zipfile.ZipFile(zip_path, \"w\") as z:\n",
        "        for root, _, files in os.walk(folder):\n",
        "            for f in files:\n",
        "                full = os.path.join(root, f)\n",
        "                z.write(full, arcname=full.replace(folder+\"/\",\"\"))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4NFkOyCLhK1o",
        "outputId": "5901c437-4942-4d68-d507-19b51c712480"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing utils/zipper.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import os\n",
        "from utils.converter import pdf_to_png\n",
        "from utils.school import school_preset\n",
        "from utils.watermark import add_watermark\n",
        "from utils.zipper import make_zip\n",
        "\n",
        "st.set_page_config(page_title=\"MassDoc Converter\", layout=\"centered\")\n",
        "\n",
        "st.title(\"🧰 MassDoc Converter\")\n",
        "st.caption(\"Upload → Convert → Download\")\n",
        "\n",
        "st.divider()\n",
        "school_mode = st.toggle(\"🏫 Aktifkan Mode Sekolah\")\n",
        "st.divider()\n",
        "\n",
        "if school_mode:\n",
        "    doc_type = st.selectbox(\n",
        "        \"Jenis Dokumen Sekolah\",\n",
        "        [\"Rapor\", \"Soal Ujian\", \"Nilai\", \"Surat Resmi\"]\n",
        "    )\n",
        "    preset = school_preset(doc_type)\n",
        "    dpi = preset[\"dpi\"]\n",
        "    prefix = preset[\"prefix\"]\n",
        "\n",
        "    school_name = st.text_input(\"Nama Sekolah\")\n",
        "    tahun = st.text_input(\"Tahun Ajaran\", \"2024/2025\")\n",
        "    watermark_text = f\"{school_name} — Arsip Resmi — {tahun}\"\n",
        "\n",
        "    st.info(f\"DPI otomatis: {dpi}\")\n",
        "else:\n",
        "    dpi = st.selectbox(\"Resolusi (DPI)\", [150,200,300])\n",
        "    watermark_text = st.text_input(\"Watermark (opsional)\")\n",
        "    prefix = \"FILE\"\n",
        "\n",
        "files = st.file_uploader(\n",
        "    \"Upload PDF\",\n",
        "    type=[\"pdf\"],\n",
        "    accept_multiple_files=True\n",
        ")\n",
        "\n",
        "if st.button(\"🚀 PROSES\") and files:\n",
        "    os.makedirs(\"output\", exist_ok=True)\n",
        "\n",
        "    bar = st.progress(0)\n",
        "    status = st.empty()\n",
        "\n",
        "    for i, f in enumerate(files):\n",
        "        status.write(f\"📄 {f.name}\")\n",
        "\n",
        "        pdf_path = f\"temp_{f.name}\"\n",
        "        with open(pdf_path,\"wb\") as out:\n",
        "            out.write(f.read())\n",
        "\n",
        "        out_dir = f\"output/{prefix}_{i+1}\"\n",
        "        os.makedirs(out_dir, exist_ok=True)\n",
        "\n",
        "        images = pdf_to_png(pdf_path, out_dir, dpi)\n",
        "\n",
        "        if watermark_text:\n",
        "            for img in images:\n",
        "                add_watermark(img, watermark_text)\n",
        "\n",
        "        bar.progress((i+1)/len(files))\n",
        "\n",
        "    zip_path = \"HASIL_KONVERSI.zip\"\n",
        "    make_zip(\"output\", zip_path)\n",
        "\n",
        "    st.success(\"✅ Selesai\")\n",
        "\n",
        "    with open(zip_path,\"rb\") as z:\n",
        "        st.download_button(\n",
        "            \"📦 Download ZIP\",\n",
        "            z,\n",
        "            file_name=\"HASIL_KONVERSI.zip\"\n",
        "        )\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IR-8yBAxhMgV",
        "outputId": "938caa14-9da0-4f7e-bf73-589417c557b1"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    }
  ]
}
