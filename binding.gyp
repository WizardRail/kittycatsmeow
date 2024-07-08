{
  "targets": [
    {
      "target_name": "ser-win",
      "sources": [ "src/ser-win.cpp" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "include"
      ],
      "libraries": [
        "-lcrypt32.lib"
      ]
    }
  ]
}