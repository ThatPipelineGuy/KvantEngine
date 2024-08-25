
-- Workspace settings
workspace "KvantEngine"
    configurations { "Debug", "Release" }
    platforms { "Win64", "Linux", "Mac" }
    location "."

    objdir "Build/Intermediate/%{cfg.platform}/%{cfg.buildcfg}"
    targetdir "Build/Binaries/%{cfg.buildcfg}/%{cfg.platform}"

    startproject "KE1"

-- Project settings
project "KvantEngine"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++17"
    location "."

    files {
        "Engine/**.h",
        "Engine/**.cpp",
        "Engine/**.inl",
        "Engine/**.hpp",
        "Engine/KVEngine.cpp",
    }

    -- Include Engine directories
    includedirs { "Engine" }

    -- link third-party libraries
    includedirs { "Engine/ThirdParty/SDL2-2.0.0/include",
                  "",
                }
    libdirs { "Engine/ThirdParty/SDL2-2.0.0/lib/x64",
              "",
            }
    links { "SDL2", "SDL2main" }

    filter "configurations:Debug"
        defines { "DEBUG" }
        symbols "On"

    filter "configurations:Release"
        defines { "NDEBUG" }
        optimize "On"

    filter "platforms:Win64"
        system "Windows"
        architecture "x64"

    filter "platforms:Linux"
        system "Linux"
        architecture "x86_64"

    filter "platforms:Mac"
        system "MacOSX"
        architecture "x86_64"
